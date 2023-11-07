include("longTermPos.jl")
include("specialFunctions.jl")
include("functions.jl")
using HTTP
using JSON


using DataFrames
using Dates

using DataFrames

mutable struct StochRSIIndicator
    close::Vector{Float64}
    window::Int
    smooth1::Int
    smooth2::Int
    fillna::Bool
    rsi::Vector{Float64}
    stochrsi::Vector{Float64}
    stochrsi_k::Vector{Float64}
    stochrsi_d::Vector{Float64}

    function StochRSIIndicator(close::Vector{Float64}, window::Int = 14, smooth1::Int = 3, smooth2::Int = 3, fillna::Bool = false)
        new(close, window, smooth1, smooth2, fillna, Float64[], Float64[], Float64[], Float64[])
        calculate_indicators()
    end
end

function calculate_indicators(self::StochRSIIndicator)
    self.rsi = rsi(self.close, self.window)
    lowest_low_rsi = rollingmin(self.rsi, self.window)
    self.stochrsi = (self.rsi - lowest_low_rsi) / (rollingmax(self.rsi, self.window) - lowest_low_rsi)
    self.stochrsi_k = rollingmean(self.stochrsi, self.smooth1)
end

function stochrsi(self::StochRSIIndicator)
    stochrsi_series = check_fillna(self.stochrsi, self.fillna)
    return DataFrame(stochrsi = stochrsi_series)
end

function stochrsi_k(self::StochRSIIndicator)
    stochrsi_k_series = check_fillna(self.stochrsi_k, self.fillna)
    return DataFrame(stochrsi_k = stochrsi_k_series)
end

function stochrsi_d(self::StochRSIIndicator)
    stochrsi_d_series = rollingmean(self.stochrsi_k, self.smooth2)
    stochrsi_d_series = check_fillna(stochrsi_d_series, self.fillna)
    return DataFrame(stochrsi_d = stochrsi_d_series)
end

function check_fillna(series, fillna)
    if fillna
        return fillmissing(series, NaN)
    end
    return series
end

function rollingmax(series, window)
    return [maximum(series[i - window + 1 : i]) for i in window:length(series)]
end

function rollingmin(series, window)
    return [minimum(series[i - window + 1 : i]) for i in window:length(series)]
end

function rollingmean(series, window)
    return [mean(series[i - window + 1 : i]) for i in window:length(series)]
end

function rsi(close, window)
    Δ = diff(close)
    gain = similar(Δ)
    loss = similar(Δ)
    for i in 1:length(Δ)
        if Δ[i] > 0
            gain[i] = Δ[i]
            loss[i] = 0.0
        else
            gain[i] = 0.0
            loss[i] = -Δ[i]
        end
    end
    average_gain = rollingmean(gain, window)
    average_loss = rollingmean(loss, window)
    rs = [average_gain[i] / average_loss[i] for i in window:length(Δ)]
    rsi_values = 100.0 .- (100.0 / (1.0 .+ rs))
    return [NaN for _ in 1:window - 1] .+ rsi_values
end


function get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2)
    close = [parse(Float64, entry["close"]) for entry in data]
    stochRSIind = StochRSIIndicator(close, window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()
end




function formatDataset2(df)
    # println(df)
    columns_to_convert = [:open, :high, :low, :close]
    df[!, columns_to_convert] .= float.(df[!, columns_to_convert])
    return df
end

function formatDataset3(data)
    # println(data)
    df = DataFrame(data)
    
    # Specify the custom datetime format to match your data
    datetime_format = DateFormat("yyyy-MM-dd HH:mm:ss")
    
    df.datetime_new = DateTime.(df.datetime, datetime_format)
    select!(df, Not(:datetime))
    rename!(df, :datetime_new => :datetime)
    
    return df
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

function simulateCrypto(df)
    printing = false
    printingSpecific = true
    totalPips = 0
    countPips = 0
    bestAvgPips = -typemax(Int)
    worstAvgPips = typemax(Int)
    # df = dropmissing(df)
    bestSpecialValue = -typemax(Int)
    worstSpecialValue = typemax(Int)
    j = -1
    k = -1
    pos = 0
    AvgPercent = 0
    nuet = 0
    countrUp = 0
    neg = 0
    BestProfilio = -typemax(Int)
    WorseProfilio = typemax(Int)
    Bestj = -1
    Bestk = -1
    worstk = -1
    worstj = -1
    bestAvgj = -1
    bestAvgk = -1
    worstAvgj = -1
    worstAvgk = -1
    BestSpecialValues = (0, 0)
    WorstSpecialValues = (0, 0)

    lst = []
    oldj = -1
    portfolio = 10
    countPos = 0
    countNeg = 0
    posPips = 0
    countr = 0
    negPips = 0
    avgPips = 0
    nowPrice = 0
    nowCount = 0
    longRunSTOCH = Dict("buySignal" => false, "luquidate" => false, "entry" => [])
    shortRunSTOCH = Dict("shortSignal" => false, "luquidate" => false, "entry" => [])

    longRunSTOCHRSI1 = Dict("buySignal" => false, "luquidate" => false, "entry" => [])
    shortRunSTOCHRSI1 = Dict("shortSignal" => false, "luquidate" => false, "entry" => [])
    previousSellStochasticRSI1 = previousBuyStochasticRSI1 = false
    lstSpecialNumsDECLINE = []
    lstSpecialNumsINCLINE = []

    SpecialValue = 0

    for j in 2:300
        if printingSpecific
            if j != oldj
                println("K: ", j)
                oldj = j
                println(lstSpecialNumsINCLINE)
                println(lstSpecialNumsDECLINE)
            end
        end

        stochRSIK1, stochRSID1 = get_StochasticRelitiveStrengthIndex(df, j, 100, 50)

        for i in 1:length(df)
            nowPrice += df[i]["close"]
            nowCount += 1

            longRunSTOCHRSI1, shortRunSTOCHRSI1 = findSelection(previousBuyStochasticRSI1, previousSellStochasticRSI1, longRunSTOCHRSI1, shortRunSTOCHRSI1, i)
            shortRunSTOCHRSI1, longRunSTOCHRSI1, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = checkLuquidation(shortRunSTOCHRSI1, longRunSTOCHRSI1, df, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)

            previousSellStochasticRSI1 = previousBuyStochasticRSI1 = false

            if stochRSIK1[i-1] >= stochRSID1[i-1] && stochRSIK1[i] < stochRSID1[i]
                previousSellStochasticRSI1 = true
            end

            if stochRSIK1[i-1] <= stochRSID1[i-1] && stochRSIK1[i] > stochRSID1[i]
                previousBuyStochasticRSI1 = true
            end

            previousBuyStochasticRSI1, previousSellStochasticRSI1 = swap(previousBuyStochasticRSI1, previousSellStochasticRSI1)

            if previousSellStochasticRSI1 && previousBuyStochasticRSI1
                previousBuyStochasticRSI1 = false
                previousSellStochasticRSI1 = false
            end
        end

        try
            percentOfTrades = round(((pos + nuet + neg) / length(df)) * 100, 2)
            AvgPrice = nowPrice / nowCount

            if printing
                try
                    println("POS/NEG RATIO: ", pos / neg)
                    println("Percentage Correct: ", round((pos / (neg + pos)) * 100, 2), "%")
                catch
                    println("ERROR 404")
                end
                println("CANDLES: ", length(df) - 2)
                println("PERCENT OF TRADES: ", percentOfTrades)
                println("protfilio: ", portfolio)
            end

            avgPips = totalPips / countPips

            if printing
                println("AVERAGE PIPS: ", totalPips / countPips)
                println("POSITIVE PIPS: ", posPips / countPos)
            end

            try
                negPip = negPips / neg
            catch
                negPip = 0
            end

            posPercent = round((posPips / pos / AvgPrice), 5)
            negPercent = round((negPip / AvgPrice), 5)
            AvgPercent = round((avgPips / AvgPrice), 5)

            if printing
                println("NEGITIVE PIPS: ", negPip)
                println("AVERAGE %: ", AvgPercent)
                println("POS %: ", posPercent)
                println("NEG %: ", negPercent)
            end

            leverage = 50

            if printing
                println("$leverageX LEVERAGE")
                println("AVERAGE %: ", AvgPercent * leverage)
                println("POS %: ", posPercent * leverage)
                println("NEG %: ", negPercent * leverage)
            end

            difference = (posPercent + negPercent)
            correctness = round((pos / (neg + pos)), 2)
            accuracy = correctness - 0.5
            tradeDecimal = percentOfTrades / 100

            if printing
                println(SpecialValue)
            end

            p = pos / (neg + pos)
            q = 1 - p
            t = ((posPips / pos / AvgPrice) * leverage / 100) + 1
            s = ((negPip / AvgPrice) * leverage / 100) + 1

            KellyCriterum = p / s - q / t

            if printing
                println("Best Bet %: ", KellyCriterum)
            end
        catch
            a = j
        end

        if avgPips * percentOfTrades > bestAvgPips && avgPips > 52000
            bestAvgPips = avgPips * percentOfTrades
            bestAvgj = j
            bestAvgk = k
        end

        if avgPips * percentOfTrades < worstAvgPips
            worstAvgPips = avgPips * percentOfTrades
            worstAvgj = j
            worstAvgk = k
        end

        if portfolio > BestProfilio
            BestProfilio = portfolio
            Bestj = j
            Bestk = k
        elseif portfolio < WorseProfilio
            WorseProfilio = portfolio
            worstj = j
            worstk = k
        end

        portfolio = 10
        negPips = 0
        posPips = 0
        totalPips = 0
        countPips = 0
        countPos = 0
        countNeg = 0

        push!(lst, portfolio)
        pos = nuet = neg = 0

        try
            SpecialValue = difference * accuracy * tradeDecimal

            if SpecialValue < 0
                push!(lstSpecialNumsDECLINE, [(j, k, c), SpecialValue])
                lstSpecialNumsDECLINE = sort(lstSpecialNumsDECLINE, by=x -> x[2])
                countr += 1

                if countr > 100
                    pop!(lstSpecialNumsDECLINE)
                end
            end

            if SpecialValue > 0
                push!(lstSpecialNumsINCLINE, [(j, k, c), SpecialValue])
                lstSpecialNumsINCLINE = sort(lstSpecialNumsINCLINE, by=x -> x[2], rev=true)
                countrUp += 1

                if countrUp > 100
                    pop!(lstSpecialNumsINCLINE)
                end
            end

            if SpecialValue > bestSpecialValue
                bestSpecialValue = SpecialValue
                BestSpecialValues = (j, k)
            end

            if SpecialValue < worstSpecialValue
                worstSpecialValue = SpecialValue
                WorstSpecialValues = (j, k)
            end
        catch
            a = j
        end
    end

    return bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue, lstSpecialNumsINCLINE, lstSpecialNumsDECLINE
end
apikey = "d6e8542914aa439e92fceaccca1c2708"
printing = true
df = (grabForex(apikey, 10))
println(df)
lst5 = []

# println(length(df))

# for i in 2:10:100
#     for j in 12:10:110
#         push!(lst5, [df, [i, j]])
#     end
# end

# println(lst5)

bestSpecialValue, worstSpecialValue, BestSpecialValues, WorstSpecialValues, worstk, worstj, bestAvgPips, bestAvgj, bestAvgk, worstAvgPips, worstAvgk, worstAvgj, AvgPercent, SpecialValue, lstSpecialNumsINCLINE, lstSpecialNumsDECLINE = simulateCrypto(df)

println("\n\nSIMULATION RESULTS: ")
println(lstSpecialNumsINCLINE)
println(lstSpecialNumsDECLINE)

open("documents/lstSpecialNumsINCLINE.txt", "w") do file
    write(file, repr(lstSpecialNumsINCLINE))
end

open("documents/lstSpecialNumsDECLINE.txt", "w") do file
    write(file, repr(lstSpecialNumsDECLINE))
end

println("\nBest Special Value: ", bestSpecialValue)
println("Values for which: ", BestSpecialValues)
println("\nWorst Special Value: ", worstSpecialValue)
println("Values for which: ", WorstSpecialValues)
end
