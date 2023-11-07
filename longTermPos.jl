module longTermPos

export checkLuquidation, findSelection


function findSelection(previousBuy, previousSell, longI, shortI, i)
    # Logic to determine how a long or short position will be opened
    if previousBuy && shortI.shortSignal
        shortI.shortSignal = false
        longI.luquidate = true
        longI.buySignal = true
        longI.entry = [i]
    elseif previousSell && longI.buySignal
        longI.buySignal = false
        shortI.luquidate = true
        shortI.shortSignal = true
        shortI.entry = [i]
    elseif previousBuy && longI.buySignal
        push!(longI.entry, i)
    elseif previousSell && shortI.shortSignal
        push!(shortI.entry, i)
    elseif previousBuy
        shortI.shortSignal = false
        longI.buySignal = true
        longI.entry = [i]
    elseif previousSell
        longI.buySignal = false
        shortI.shortSignal = true
        shortI.entry = [i]
    end
    return longI, shortI
end


function checkLuquidation(shortI, longI, data, i, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg)
    if shortI.luquidate
        BuyOrSell = false
        pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = findPos(data, longI.entry, i, BuyOrSell, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg) # Logic to close short position
        longI.entry = []
        shortI.luquidate = false
    end
    if longI.luquidate
        BuyOrSell = true
        pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg = findPos(data, shortI.entry, i, BuyOrSell, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg) # Logic to close long position
        shortI.entry = []
        longI.luquidate = false
    end
    return shortI, longI, pos, nuet, neg, portfolio, totalPips, countPips, posPips, countPos, negPips, countNeg
end

end