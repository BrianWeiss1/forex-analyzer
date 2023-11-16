using DataFrames
using Statistics
using Dates
using Random
using HTTP
using JSON
using LinearAlgebra
using DataFrames
using Statistics
using TimeSeries

function RSI(close_prices, period::Int)
    # Calculate daily price changes
    delta = close_prices[:, "close"]
    # Calculate gains and losses
    gains = zeros(Float64, length(delta))
    losses = zeros(Float64, length(delta))

    for i in 1:length(delta)
        if delta[i] > 0
            gains[i] = delta[i]
        else
            losses[i] = -delta[i]
        end
    end

    # Calculate average gains and losses over the specified period
    avg_gains = mean(gains[1:period])
    avg_losses = mean(losses[1:period])

    # Calculate initial RS and RSI
    rs = avg_gains / max(avg_losses, 1e-10)  # To avoid division by zero
    rsi = 100 - (100 / (1 + rs))

    # Calculate RSI for the rest of the data
    for i in period+1:length(delta)
        gain = ifelse(delta[i] > 0, delta[i], 0)
        loss = ifelse(delta[i] < 0, -delta[i], 0)

        avg_gains = ((period - 1) * avg_gains + gain) / period
        avg_losses = ((period - 1) * avg_losses + loss) / period

        rs = avg_gains / max(avg_losses, 1e-10)
        rsi = [rsi; 100 - (100 / (1 + rs))]
    end

    return rsi
end

function SMA(data, window::Int)
    return [mean(data[i:min(i+window-1, end)]) for i in 1:length(data)-window+1]
end




function get_StochasticRelitiveStrengthIndex(data, period::Int = 14, k::Int = 3, d::Int = 3)
    rsi_values = RSI(data, period)
    k_values = SMA(rsi_values, k)
    d_values = SMA(k_values, d)

    stochrsi_values = (k_values - d_values) / 100

    return stochrsi_values
end




function formatDataset2(df::DataFrame)::DataFrame
    columns_to_convert = [:open, :high, :low, :close]
    for col in columns_to_convert
        df[!, col] = parse.(Float64, df[!, col])
    end
    return df
end


function formatDataset3(data::Vector)::DataFrame
    df = DataFrame(data)
    df.datetime .= DateTime.(df.datetime, dateformat"yyyy-mm-dd HH:MM:SS")
    return df
end

function findPos(data, pastI, currentI, BuyOrSell, pos, nuet, neg, posPips, negPips)
    if BuyOrSell
        if data[currentI] > data[pastI[1]]
            pos += 1
            currentPipChange = abs((data[currentI] * 100) - (100 * data[pastI[1]]))
            currentPrice = data[currentI]
            percentChange = currentPipChange / currentPrice
            changeDecimal = percentChange / 100
            posPips += currentPipChange
        elseif data[currentI] == data[pastI[1]]
            nuet += 1
        else
            neg += 1
            currentPipChange = abs((100 * data[pastI[1]]) - (data[currentI] * 100))
            currentPrice = data[currentI]
            percentChange = currentPipChange / currentPrice
            changeDecimal = -percentChange / 100
            negPips -= currentPipChange
        end
    else
        if data[currentI] < data[pastI[1]]
            pos += 1
            currentPipChange = abs((data[currentI] * 100) - (100 * data[pastI[1]]))
            currentPrice = data[currentI]
            percentChange = currentPipChange / currentPrice
            changeDecimal = percentChange / 100
            posPips += currentPipChange
        elseif data[currentI] == data[pastI[1]]
            nuet += 1
        else
            neg += 1
            currentPipChange = abs((100 * data[pastI[1]]) - (data[currentI] * 100))
            currentPrice = data[currentI]
            percentChange = currentPipChange / currentPrice
            changeDecimal = -percentChange / 100
            negPips -= currentPipChange
        end
        pastI = []
    end
    return pos, nuet, neg, posPips, negPips
end

function findSelection(previousBuy, previousSell, longI, shortI, i)
    if previousBuy && shortI["shortSignal"]
        shortI["shortSignal"] = false
        longI["luquidate"] = true
        longI["buySignal"] = true
        longI["entry"] = [i]
    elseif previousSell && longI["buySignal"]
        longI["buySignal"] = false
        shortI["luquidate"] = true
        shortI["shortSignal"] = true
        shortI["entry"] = [i]
    elseif previousBuy && longI["buySignal"]
        push!(longI["entry"], i)
    elseif previousSell && shortI["shortSignal"]
        push!(shortI["entry"], i)
    elseif previousBuy
        shortI["shortSignal"] = false
        longI["buySignal"] = true
        longI["entry"] = [i]
    elseif previousSell
        longI["buySignal"] = false
        shortI["shortSignal"] = true
        shortI["entry"] = [i]
    end
    return longI, shortI
end

function checkLuquidation(shortI, longI, data, i, pos, nuet, neg, posPips, negPips)
    if shortI["luquidate"]
        BuyOrSell = false
        pos, nuet, neg, posPips, negPips = findPos(data, longI["entry"], i, BuyOrSell, pos, nuet, neg, posPips, negPips)
        longI["entry"] = []
        shortI["luquidate"] = false
    end
    if longI["luquidate"]
        BuyOrSell = true
        pos, nuet, neg, posPips, negPips = findPos(data, shortI["entry"], i, BuyOrSell, pos, nuet, neg, posPips, negPips)
        shortI["entry"] = []
        longI["luquidate"] = false
    end
    return shortI, longI, pos, nuet, neg, posPips, negPips
end

function grabForex(apikey::String, outputsize::Int = 30)
    symbol = "EUR/USD"
    interval = "30min"

    base_url = "https://api.twelvedata.com/time_series"
    url = "$base_url?symbol=$symbol&interval=$interval&outputsize=$outputsize&apikey=$apikey"
    
    # Send an HTTP GET request to the API
    response = HTTP.get(url)
    
    if response.status == 200
        data = JSON.parse(String(response.body))
        
        if data["status"] == "ok"
            values = data["values"]
            return values
        else
            println("API request failed: ", data["status"])
        end
    else
        println("HTTP request failed with status code: ", response.status)
    end
end



function simulateCrypto(df::DataFrame, amountTo::Int, a::Bool, b::Bool, c::Bool, aVal::Int, bVal::Int, cVal::Int, increment::Int)
    printing = false
    printingSpecific = true
    df = dropmissing(df)
    bestSpecialValue = typemax(Int)
    worstSpecialValue = typemin(Int)
    j = -1
    k = -1
    pos = 0
    nuet = 0
    neg = 0
    BestSpecialValues = (0, 0)
    WorstSpecialValues = (0, 0)
    oldj = -1
    posPips = 0
    negPips = 0
    nowPrice = 0
    nowCount = 0
    longRunSTOCHRSI1 = Dict("buySignal" => false, "luquidate" => false, "entry" => [])
    shortRunSTOCHRSI1 = Dict("shortSignal" => false, "luquidate" => false, "entry" => [])
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = false
    SpecialValue = 0
    
    for j in 2:increment:amountTo
        if printingSpecific
            if j != oldj
                oldj = j
            end
        end

        if a
            stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, j, bVal, cVal)
        elseif b
            stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, aVal, j, cVal)
        elseif c
            stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, aVal, bVal, j)
        else
            stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, j, 100, 680)
        end

        stochRSIK1 = convert(Array, stochRSIK1)
        stochRSID1 = convert(Array, stochRSID1)
        closeData = convert(Array, df[:, "close"])

        for i in 1:length(df)
            nowPrice += closeData[i]
            nowCount += 1

            # --------STOCH1RSI----------#
            longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i)
            shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, posPips, negPips = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, closeData, i, pos, nuet, neg, posPips, negPips)

            previousSellStochasticRSI1 = previousBuyStochasticRSI1 = false

            if stochRSIK1[i - 1] > stochRSID1[i - 1] && stochRSIK1[i] < stochRSID1[i]
                previousSellStochasticRSI1 = true
            end

            if stochRSIK1[i - 1] < stochRSID1[i - 1] && stochRSIK1[i] > stochRSID1[i]
                previousBuyStochasticRSI1 = true
            end

            if previousSellStochasticRSI1 && previousBuyStochasticRSI1
                previousBuyStochasticRSI1 = false
                previousSellStochasticRSI1 = false
            end
            # --------STOCH1RSI----------#
        end
        println(pos)
        try
            percentOfTrades = round(((pos + nuet + neg) / length(df)) * 100, digits=2)
            AvgPrice = nowPrice / nowCount

            negPip = ifelse(neg != 0, negPips / neg, 0)

            posPercent = round((posPips / pos / AvgPrice), digits=5)
            negPercent = round((negPip / AvgPrice), digits=5)

            difference = (posPercent + negPercent)
            correctness = round((pos / (neg + pos)), digits=2)
            accuracy = correctness - 0.5
            tradeDecimal = percentOfTrades / 100
        catch e
            if printing
                println("ERROR GO BRRRR")
            end
        end

        pos = nuet = neg = 0
        println(difference)
        try
            println(difference)
            println(accuracy)
            println(tradeDecimal)
            SpecialValue = difference * accuracy * tradeDecimal
            if SpecialValue > bestSpecialValue
                bestSpecialValue = SpecialValue
                BestSpecialValues = (j, k)
            end

            if SpecialValue < worstSpecialValue
                worstSpecialValue = SpecialValue
                WorstSpecialValues = (j, k)
            end
        catch e
            if printing
                println("ERROR")
            end
        end
        negPips = 0
        posPips = 0
    end
    return bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues
end


function main()
    df = formatDataset2(formatDataset3(grabForex("d6e8542914aa439e92fceaccca1c2708", 5000)))

    a = b = c = false
    aVal = bVal = cVal = 50
    i = 50
    stochValues = []
    lastBestVal = -1
    amountTo = 1400
    countRep = 0

    while true
        a = b = c = false
        abOrC = rand(0:2)
        if abOrC == 0
            a = true
        elseif abOrC == 1
            b = true
        else
            c = true
        end

        aVal = rand(1:1000)
        bVal = rand(1:1000)
        cVal = rand(1:1000)

        amountTo = 1400
        repeatA = repeatB = repeatC = false
        onceA = onceB = onceC = false

        while true
            bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues = simulateCrypto(df, amountTo, a, b, c, aVal, bVal, cVal, 5)
            randomNum = rand(0:1)

            if abs(bestSpecialValue) > abs(worstSpecialValue)
                bestVal = BestSpecialValues[1]
                bestPer = bestSpecialValue
            else
                bestVal = WorstSpecialValues[1]
                bestPer = worstSpecialValue
            end

            if a
                onceA = true
                a = false

                if aVal == bestVal
                    repeatA = true
                else
                    repeatA = false
                    repeatB = false
                    repeatC = false
                end

                aVal = bestVal

                if (randomNum == 1 || repeatC) && (!repeatB)
                    b = true
                elseif (randomNum == 0 || repeatB) && (!repeatC)
                    c = true
                end
            elseif b
                onceB = true

                if bVal == bestVal
                    repeatB = true
                else
                    repeatA = false
                    repeatB = false
                    repeatC = false
                end

                b = false
                bVal = bestVal

                if (randomNum == 1 || repeatC) && (!repeatA)
                    a = true
                elseif (randomNum == 0 || repeatA) && (!repeatC)
                    c = true
                end
            elseif c
                onceC = true

                if cVal == bestVal
                    repeatC = true
                else
                    repeatA = false
                    repeatB = false
                    repeatC = false
                end

                c = false
                cVal = bestVal

                if (randomNum == 1 || repeatB) && (!repeatA)
                    a = true
                elseif (randomNum == 0 || repeatA) && (!repeatB)
                    b = true
                end
            else
                println("ERROR: No value for a b c")
            end

            if repeatA && repeatB && repeatC
                break
            end

            if onceC && onceB && onceA
                amountTo = Int(max(aVal, bVal, cVal) * 2)
            end

            lastBestVal = bestVal
        end

        repeatA = repeatB = repeatC = false
        a = b = c = false
        abOrC = rand(0:2)

        if abOrC == 0
            a = true
        elseif abOrC == 1
            b = true
        else
            c = true
        end

        onceA = onceB = onceC = false

        while true
            bestSpecialValue, BestSpecialValues, worstSpecialValue, WorstSpecialValues = simulateCrypto(df, amountTo, a, b, c, aVal, bVal, cVal, 1)
            randomNum = rand(0:1)

            if abs(bestSpecialValue) > abs(worstSpecialValue)
                bestVal = BestSpecialValues[1]
                bestPer = bestSpecialValue
            else
                bestVal = WorstSpecialValues[1]
                bestPer = worstSpecialValue
            end

            if a
                onceA = true
                a = false

                if aVal  == bestVal
                    repeatA = true
                else
                    repeatA = false
                    repeatB = false
                    repeatC = false
                end

                aVal = bestVal

                if (randomNum == 1 || repeatC) && (!repeatB)
                    b = true
                elseif (randomNum == 0 || repeatB) && (!repeatC)
                    c = true
                end
            elseif b
                onceB = true

                if bVal == bestVal
                    repeatB = true
                else
                    repeatA = false
                    repeatB = false
                    repeatC = false
                end

                b = false
                bVal = bestVal

                if (randomNum == 1 || repeatC) && (!repeatA)
                    a = true
                elseif (randomNum == 0 || repeatA) && (!repeatC)
                    c = true
                end
            elseif c
                onceC = true

                if cVal == bestVal
                    repeatC = true
                else
                    repeatA = false
                    repeatB = false
                    repeatC = false
                end

                c = false
                cVal = bestVal

                if (randomNum == 1 || repeatB) && (!repeatA)
                    a = true
                elseif (randomNum == 0 || repeatA) && (!repeatB)
                    b = true
                end
            else
                println("ERROR: No value for a b c")
            end

            if repeatA && repeatB && repeatC
                println("get_StochasticRelitiveStrengthIndex(df, $aVal, $bVal, $cVal)")
                push!(stochValues, [bestPer, (aVal, bVal, cVal)])
                break
            end

            if onceC && onceB && onceA
                amountTo = Int(max(aVal, bVal, cVal) * 2)
            end

            lastBestVal = bestVal
        end

        # println(stochValues)
    end
end

# Call the main function
main()
