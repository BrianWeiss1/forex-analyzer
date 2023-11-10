module functions

export get_StochasticRelitiveStrengthIndex



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
        run()
    end
end

function run(self::StochRSIIndicator)
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
    close = [entry["close"] for entry in data]
    stochRSIind = StochRSIIndicator(close, window, smooth1, smooth2)
    return stochRSIind.stochrsi_k(), stochRSIind.stochrsi_d()
end



end