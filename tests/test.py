# //@version=4
# // Created By Lij_MC
# // 
# // Use as a supplementary Indicator to confirm your entries, but it is as good on it's own.
# //
# // The indicator consists of 3 different Trend Meters and 2 Trend Bars which are used to confirm trend 
# //
# // As a bonus Wave Trend Signals are marked as well, these are very powerful however please use with caution 
# //
# // How to Use 
# //
# // Look for Support or Resistance Levels for price to be attracted to
# //
# // Be CAUTIOUS of trading BREAKOUTs as 9 out of 10 Breakouts Fail
# //
# // Find confluence with other indicators
# //
# // Enter Long above the Setup Bar
# //
# // Enter Short Below the Setup Bar


# (title="Trend Meter")

# // Inputs / Menus

PosNegPressure = input("Pos / Neg Pressure", tooltip= "Positive Pressure   = RSI14 and Wave Trend Over Sold with WT Delta Pointing Up                                                               Negative Pressure = RSI14 and Wave Trend Over Bought with WT Delta Pointing Down", group = "Signals")

TMSetups       = input("Trend Meter Signal", tooltip="All 3 Trend Meters Now Align", group = "Signals")

TMSetupsANDWT  = input("Wave Trend Cross Aligns with Trend Meter Signal",            group = "Signals")

 

TrendBar1 = input(title="Trend Meter 1", defval="MACD Crossover - Fast - 8, 21, 5", options=["MACD Crossover - 12, 26, 9", "MACD Crossover - Fast - 8, 21, 5", "Mom Dad Cross (Top Dog Trading)", "RSI Signal Line Cross - RSI 13, Sig 21", "RSI 13: > or < 50", "RSI 5: > or < 50", "Trend Candles", "N/A"],   group = "Trend Meters")  // "MA Crossover", "DAD Direction (Top Dog Trading)",

TrendBar2 = input(title="Trend Meter 2", defval="RSI 13: > or < 50", options=["MACD Crossover - 12, 26, 9", "MACD Crossover - Fast - 8, 21, 5", "Mom Dad Cross (Top Dog Trading)", "RSI Signal Line Cross - RSI 13, Sig 21", "RSI 13: > or < 50", "RSI 5: > or < 50", "Trend Candles", "N/A"],                  group = "Trend Meters")  // "MA Crossover", "DAD Direction (Top Dog Trading)",

TrendBar3 = input(title="Trend Meter 3", defval="RSI 5: > or < 50", options=["MACD Crossover - 12, 26, 9", "MACD Crossover - Fast - 8, 21, 5", "Mom Dad Cross (Top Dog Trading)", "RSI Signal Line Cross - RSI 13, Sig 21", "RSI 13: > or < 50", "RSI 5: > or < 50", "Trend Candles", "N/A"],                   group = "Trend Meters")  // "MA Crossover", "DAD Direction (Top Dog Trading)",






RSIMC = rsi(close, 14)


ap = hlc3  // input(hlc3, "Wave Trend - Source")
n1 = 9  //input(9,    "Wave Trend - WT Channel Length")
n2 = 12  // input(12,   "Wave Trend - WT Average Length")
esa = ema(ap, n1)
de = ema(abs(ap - esa), n1)
ci = (ap - esa) / (0.015 * de)
tci = ema(ci, n2)
wt1 = tci
wt2 = sma(wt1, 3)

YellowWave= wt1 -wt2
// Wave Trend - Overbought & Oversold lines

obLevel2 = 60  // input( 60,  "Wave Trend - WT Very Overbought")
obLevel = 50  // input( 50,  "Wave Trend - WT Overbought")
osLevel = -50  // input(-50,  "Wave Trend - WT Oversold")
osLevel2 = -60  // input(-60,  "Wave Trend - WT Very Oversold")

// Wave Trend - Conditions

WTCross = cross(wt1, wt2)
WTCrossUp = wt2 - wt1 <= 0
WTCrossDown = wt2 - wt1 >= 0
WTOverSold = wt2 <= osLevel2
WTOverBought = wt2 >= obLevel2


// MA Inputs

ShowTrendBar1 = input(true, "Trend Bar 1", group = "Trend Bar 1", inline = "Trend Bar 1")

ShowTrendBar2 = input(true, "Trend Bar 2", group = "Trend Bar 2", inline = "Trend Bar 2")


TrendBar4 = input(title="", defval="MA Crossover", options=["MA Crossover", "MA Direction - Fast MA - TB1", "MA Direction - Slow MA - TB1"], group = "Trend Bar 1", inline = "Trend Bar 1")  //  "MACD Crossover - 12, 26 9", "MACD Crossover - Fast - 8, 21, 5", "DAD Direction (Top Dog Trading)",

TrendBar5 = input(title="", defval="MA Crossover", options=["MA Crossover", "MA Direction - Fast MA - TB2", "MA Direction - Slow MA - TB2"], group = "Trend Bar 2", inline = "Trend Bar 2")  //  "MACD Crossover - 12, 26 9", "MACD Crossover - Fast - 8, 21, 5", "DAD Direction (Top Dog Trading)",



MA1_Length = input(5,  title='Fast MA', minval=1,                             group = "Trend Bar 1", inline = "TB1 Fast")
MA1_Type   = input(    title='',        defval="EMA", options=["EMA", "SMA"], group = "Trend Bar 1", inline = "TB1 Fast")

MA2_Length = input(11, title='Slow MA', minval=1,                             group = "Trend Bar 1", inline = "TB1 Slow")
MA2_Type   = input(    title='',        defval="EMA", options=["EMA", "SMA"], group = "Trend Bar 1", inline = "TB1 Slow")

MA3_Length = input(13, title='Fast MA', minval=1,                             group = "Trend Bar 2", inline = "TB2 Fast")
MA3_Type   = input(    title='',        defval="EMA", options=["EMA", "SMA"], group = "Trend Bar 2", inline = "TB2 Fast")

MA4_Length = input(36, title='Slow MA', minval=1,                             group = "Trend Bar 2", inline = "TB2 Slow")
MA4_Type   = input(    title='',        defval="SMA", options=["EMA", "SMA"], group = "Trend Bar 2", inline = "TB2 Slow")


// MA Calculations

Close = close   //security(syminfo.tickerid, timeframe.period, close, barmerge.lookahead_off)


MA1 = if MA1_Type == "SMA"
    sma(Close, MA1_Length)
else
    ema(Close, MA1_Length)


MA2 = if MA2_Type == "SMA"
    sma(Close, MA2_Length)
else
    ema(Close, MA2_Length)


MA3 = if MA3_Type == "SMA"
    sma(Close, MA3_Length)
else
    ema(Close, MA3_Length)


MA4 = if MA4_Type == "SMA"
    sma(Close, MA4_Length)
else
    ema(Close, MA4_Length)


// MA Crossover Condition

MACrossover1 = MA1 > MA2 ? 1 : 0

MACrossover2 = MA3 > MA4 ? 1 : 0

// MA Direction Condition

MA1Direction = MA1 > MA1[1] ? 1 : 0

MA2Direction = MA2 > MA2[1] ? 1 : 0

MA3Direction = MA3 > MA3[1] ? 1 : 0

MA4Direction = MA4 > MA4[1] ? 1 : 0

// MA Direction Change Condition

MA1PositiveDirectionChange = MA1Direction and not MA1Direction[1] ? 1 : 0

MA2PositiveDirectionChange = MA2Direction and not MA2Direction[1] ? 1 : 0

MA3PositiveDirectionChange = MA3Direction and not MA3Direction[1] ? 1 : 0

MA4PositiveDirectionChange = MA4Direction and not MA4Direction[1] ? 1 : 0


MA1NegativeDirectionChange = not MA1Direction and MA1Direction[1] ? 1 : 0

MA2NegativeDirectionChange = not MA2Direction and MA2Direction[1] ? 1 : 0

MA3NegativeDirectionChange = not MA3Direction and MA3Direction[1] ? 1 : 0

MA4NegativeDirectionChange = not MA4Direction and MA4Direction[1] ? 1 : 0


// MACD and MOM & DAD - Top Dog Trading

// Standard MACD Calculations

MACDfastMA = 12
MACDslowMA = 26
MACDsignalSmooth = 9


MACDLine = ema(close, MACDfastMA) - ema(close, MACDslowMA)

SignalLine = ema(MACDLine, MACDsignalSmooth)

MACDHistogram = MACDLine - SignalLine


// MACD- Background Color Change Condition

MACDHistogramCross = MACDHistogram > 0 ? 1 : 0

MACDLineOverZero = MACDLine > 0 ? 1 : 0

MACDLineOverZeroandHistogramCross = MACDHistogramCross and MACDLineOverZero ? 1 : 0

MACDLineUnderZeroandHistogramCross = not MACDHistogramCross and not MACDLineOverZero ? 1 : 0


// Fast MACD Calculations

FastMACDfastMA = 8
FastMACDslowMA = 21
FastMACDsignalSmooth = 5


FastMACDLine = ema(close, FastMACDfastMA) - ema(close, FastMACDslowMA)

FastSignalLine = ema(FastMACDLine, FastMACDsignalSmooth)

FastMACDHistogram = FastMACDLine - FastSignalLine

// Fast MACD- Background Color Change Condition

FastMACDHistogramCross = FastMACDHistogram > 0 ? 1 : 0

FastMACDLineOverZero = FastMACDLine > 0 ? 1 : 0

FastMACDLineOverZeroandHistogramCross = FastMACDHistogramCross and FastMACDLineOverZero ? 1 : 0

FastMACDLineUnderZeroandHistogramCross = not FastMACDHistogramCross and not FastMACDLineOverZero ? 1 : 0


// Top Dog Trading - Mom Dad Calculations

TopDog_Fast_MA = 5
TopDog_Slow_MA = 20
TopDog_Sig = 30


TopDogMom = ema(close, TopDog_Fast_MA) - ema(close, TopDog_Slow_MA)

TopDogDad = ema(TopDogMom, TopDog_Sig)

// Top Dog Dad - Background Color Change Condition

TopDogDadDirection = TopDogDad > TopDogDad[1] ? 1 : 0

TopDogMomOverDad = TopDogMom > TopDogDad ? 1 : 0

TopDogMomOverZero = TopDogMom > 0 ? 1 : 0

TopDogDadDirectandMomOverZero = TopDogDadDirection and TopDogMomOverZero ? 1 : 0

TopDogDadDirectandMomUnderZero = not TopDogDadDirection and not TopDogMomOverZero ? 1 : 0



////// Trend Barmeter Calculations //////

// UCS_Trend / Trend Candles Trend Barmeter Calculations

//UCS_Trend by ucsgears copy Trend Candles
//Interpretation of TTM Trend bars. It is really close to the actual. 

haclose = ohlc4
haopen = 0.0
haopen := na(haopen[1]) ? (open + close) / 2 : (haopen[1] + haclose[1]) / 2
//hahigh = max(high, max(haopen, haclose))
//halow = min(low, min(haopen, haclose))

ccolor = haclose - haopen > 0 ? 1 : 0

inside6 = haopen <= max(haopen[6], haclose[6]) and haopen >= min(haopen[6], haclose[6]) and 
   haclose <= max(haopen[6], haclose[6]) and haclose >= min(haopen[6], haclose[6]) ? 
   1 : 0

inside5 = haopen <= max(haopen[5], haclose[5]) and haopen >= min(haopen[5], haclose[5]) and 
   haclose <= max(haopen[5], haclose[5]) and haclose >= min(haopen[5], haclose[5]) ? 
   1 : 0

inside4 = haopen <= max(haopen[4], haclose[4]) and haopen >= min(haopen[4], haclose[4]) and 
   haclose <= max(haopen[4], haclose[4]) and haclose >= min(haopen[4], haclose[4]) ? 
   1 : 0

inside3 = haopen <= max(haopen[3], haclose[3]) and haopen >= min(haopen[3], haclose[3]) and 
   haclose <= max(haopen[3], haclose[3]) and haclose >= min(haopen[3], haclose[3]) ? 
   1 : 0

inside2 = haopen <= max(haopen[2], haclose[2]) and haopen >= min(haopen[2], haclose[2]) and 
   haclose <= max(haopen[2], haclose[2]) and haclose >= min(haopen[2], haclose[2]) ? 
   1 : 0

inside1 = haopen <= max(haopen[1], haclose[1]) and haopen >= min(haopen[1], haclose[1]) and 
   haclose <= max(haopen[1], haclose[1]) and haclose >= min(haopen[1], haclose[1]) ? 
   1 : 0


colorvalue = inside6 ? ccolor[6] : inside5 ? ccolor[5] : inside4 ? ccolor[4] : 
   inside3 ? ccolor[3] : inside2 ? ccolor[2] : inside1 ? ccolor[1] : ccolor

TrendBarTrend_Candle_Color = colorvalue ? #288a75 : color.red

TrendBarTrend_Candle = colorvalue ? 1 : 0


// RSI 5 Trend Barmeter Calculations

RSI5 = rsi(close, 5)

RSI5Above50 = RSI5 > 50 ? 1 : 0

RSI5Color = RSI5Above50 ? #288a75 : color.red

TrendBarRSI5Color = RSI5Above50 ? #288a75 : color.red


// RSI 5 Trend Barmeter Calculations

RSI13 = rsi(close, 13)


// Linear Regression Calculation For RSI Signal Line

SignalLineLength1 = 21

x = bar_index
y = RSI13
x_ = sma(x, SignalLineLength1)
y_ = sma(y, SignalLineLength1)
mx = stdev(x, SignalLineLength1)
my = stdev(y, SignalLineLength1)
c = correlation(x, y, SignalLineLength1)
slope = c * (my / mx)
inter = y_ - slope * x_
LinReg1 = x * slope + inter


RSISigDirection = LinReg1 > LinReg1[1] ? 1 : 0

RSISigCross = RSI13 > LinReg1 ? 1 : 0

RSI13Above50 = RSI13 > 50 ? 1 : 0


// Trend Barmeter Color Calculation

RSI13Color = RSI13Above50 ? #288a75 : color.red

TrendBarRSI13Color = RSI13Above50 ? #288a75 : color.red

TrendBarRSISigCrossColor = RSISigCross ? #288a75 : color.red

TrendBarMACDColor = MACDHistogramCross ? #288a75 : color.red

TrendBarFastMACDColor = FastMACDHistogramCross ? #288a75 : color.red

TrendBarMACrossColor = MACrossover1 ? #288a75 : color.red

TrendBarMomOverDadColor = TopDogMomOverDad ? #288a75 : color.red

TrendBarDadDirectionColor = TopDogDadDirection ? #288a75 : color.red


TrendBar1Result = TrendBar1 == "MA Crossover" ? MACrossover1 : 
   TrendBar1 == "MACD Crossover - 12, 26, 9" ? MACDHistogramCross : 
   TrendBar1 == "MACD Crossover - Fast - 8, 21, 5" ? FastMACDHistogramCross : 
   TrendBar1 == "Mom Dad Cross (Top Dog Trading)" ? TopDogMomOverDad : 
   TrendBar1 == "DAD Direction (Top Dog Trading)" ? TopDogDadDirection : 
   TrendBar1 == "RSI Signal Line Cross - RSI 13, Sig 21" ? RSISigCross : 
   TrendBar1 == "RSI 5: > or < 50" ? RSI5Above50 : 
   TrendBar1 == "RSI 13: > or < 50" ? RSI13Above50 : 
   TrendBar1 == "Trend Candles" ? TrendBarTrend_Candle : na

TrendBar2Result = TrendBar2 == "MA Crossover" ? MACrossover1 : 
   TrendBar2 == "MACD Crossover - 12, 26, 9" ? MACDHistogramCross : 
   TrendBar2 == "MACD Crossover - Fast - 8, 21, 5" ? FastMACDHistogramCross : 
   TrendBar2 == "Mom Dad Cross (Top Dog Trading)" ? TopDogMomOverDad : 
   TrendBar2 == "DAD Direction (Top Dog Trading)" ? TopDogDadDirection : 
   TrendBar2 == "RSI Signal Line Cross - RSI 13, Sig 21" ? RSISigCross : 
   TrendBar2 == "RSI 5: > or < 50" ? RSI5Above50 : 
   TrendBar2 == "RSI 13: > or < 50" ? RSI13Above50 : 
   TrendBar2 == "Trend Candles" ? TrendBarTrend_Candle : na

TrendBar3Result = TrendBar3 == "MA Crossover" ? MACrossover1 : 
   TrendBar3 == "MACD Crossover - 12, 26, 9" ? MACDHistogramCross : 
   TrendBar3 == "MACD Crossover - Fast - 8, 21, 5" ? FastMACDHistogramCross : 
   TrendBar3 == "Mom Dad Cross (Top Dog Trading)" ? TopDogMomOverDad : 
   TrendBar3 == "DAD Direction (Top Dog Trading)" ? TopDogDadDirection : 
   TrendBar3 == "RSI Signal Line Cross - RSI 13, Sig 21" ? RSISigCross : 
   TrendBar3 == "RSI 5: > or < 50" ? RSI5Above50 : 
   TrendBar3 == "RSI 13: > or < 50" ? RSI13Above50 : 
   TrendBar3 == "Trend Candles" ? TrendBarTrend_Candle : na


TrendBars2Positive = TrendBar1Result and TrendBar2Result or TrendBar1Result and TrendBar3Result or 
   TrendBar2Result and TrendBar3Result ? 1 : 0

TrendBars2Negative = not TrendBar1Result and not TrendBar2Result or 
   not TrendBar1Result and not TrendBar3Result or 
   not TrendBar2Result and not TrendBar3Result ? 1 : 0


TrendBars3Positive =     TrendBar1Result and     TrendBar2Result and     TrendBar3Result ? 1 : 0

TrendBars3Negative = not TrendBar1Result and not TrendBar2Result and not TrendBar3Result ? 1 : 0


PositiveWaveTrendCross = WTCross and WTCrossUp

NegativeWaveTrendCross = WTCross and WTCrossDown


///////////////////////////////////////////////////////////////////////////////////////////////////////////////

BackgroundColorChangePositive = TrendBars3Positive and not TrendBars3Positive[1]
BackgroundColorChangeNegative = TrendBars3Negative and not TrendBars3Negative[1]

// Signals Color Calculations


MSBar2Color = BackgroundColorChangePositive ? #288a75 : 
   BackgroundColorChangeNegative ? color.red : na


// Trend Barmeter Color Assignments

TrendBar1Color = TrendBar1 == "N/A" ? na : 
   TrendBar1 == "MACD Crossover - 12, 26, 9" ? TrendBarMACDColor : 
   TrendBar1 == "MACD Crossover - Fast - 8, 21, 5" ? TrendBarFastMACDColor : 
   TrendBar1 == "Mom Dad Cross (Top Dog Trading)" ? TrendBarMomOverDadColor : 
   TrendBar1 == "DAD Direction (Top Dog Trading)" ? TrendBarDadDirectionColor : 
   TrendBar1 == "RSI Signal Line Cross - RSI 13, Sig 21" ? TrendBarRSISigCrossColor : 
   TrendBar1 == "RSI 5: > or < 50" ? TrendBarRSI5Color : 
   TrendBar1 == "RSI 13: > or < 50" ? TrendBarRSI13Color : 
   TrendBar1 == "Trend Candles" ? TrendBarTrend_Candle_Color : 
   TrendBar1 == "MA Crossover" ? TrendBarMACrossColor : na

TrendBar2Color = TrendBar2 == "N/A" ? na : 
   TrendBar2 == "MACD Crossover - 12, 26, 9" ? TrendBarMACDColor : 
   TrendBar2 == "MACD Crossover - Fast - 8, 21, 5" ? TrendBarFastMACDColor : 
   TrendBar2 == "Mom Dad Cross (Top Dog Trading)" ? TrendBarMomOverDadColor : 
   TrendBar2 == "DAD Direction (Top Dog Trading)" ? TrendBarDadDirectionColor : 
   TrendBar2 == "RSI Signal Line Cross - RSI 13, Sig 21" ? TrendBarRSISigCrossColor : 
   TrendBar2 == "RSI 5: > or < 50" ? TrendBarRSI5Color : 
   TrendBar2 == "RSI 13: > or < 50" ? TrendBarRSI13Color : 
   TrendBar2 == "Trend Candles" ? TrendBarTrend_Candle_Color : 
   TrendBar2 == "MA Crossover" ? TrendBarMACrossColor : na

TrendBar3Color = TrendBar3 == "N/A" ? na : 
   TrendBar3 == "MACD Crossover - 12, 26, 9" ? TrendBarMACDColor : 
   TrendBar3 == "MACD Crossover - Fast - 8, 21, 5" ? TrendBarFastMACDColor : 
   TrendBar3 == "Mom Dad Cross (Top Dog Trading)" ? TrendBarMomOverDadColor : 
   TrendBar3 == "DAD Direction (Top Dog Trading)" ? TrendBarDadDirectionColor : 
   TrendBar3 == "RSI Signal Line Cross - RSI 13, Sig 21" ? TrendBarRSISigCrossColor : 
   TrendBar3 == "RSI 5: > or < 50" ? TrendBarRSI5Color : 
   TrendBar3 == "RSI 13: > or < 50" ? TrendBarRSI13Color : 
   TrendBar3 == "Trend Candles" ? TrendBarTrend_Candle_Color : 
   TrendBar3 == "MA Crossover" ? TrendBarMACrossColor : na


CrossoverType2 = TrendBar4 == "DAD Direction (Top Dog Trading)" ? TopDogDadDirection : 
   TrendBar4 == "MACD Crossover" ? MACDHistogramCross : 
   TrendBar4 == "MA Direction - Fast MA - TB1" ? MA1Direction : 
   TrendBar4 == "MA Direction - Slow MA - TB1" ? MA2Direction : MACrossover1

color_1 = color.new(color.green, 15)
color_2 = color.new(color.red, 20)
TrendBar4Color1 = TrendBar4 == "N/A" ? na : CrossoverType2 ? color_1 : color_2


CrossoverType3 = TrendBar5 == "DAD Direction (Top Dog Trading)" ? TopDogDadDirection : 
   TrendBar5 == "MACD Crossover" ? MACDHistogramCross : 
   TrendBar5 == "MA Direction - Fast MA - TB2" ? MA3Direction : 
   TrendBar5 == "MA Direction - Slow MA - TB2" ? MA4Direction : MACrossover2

color_3 = color.new(color.green, 15)
color_4 = color.new(color.red, 20)
TrendBar5Color1 = TrendBar5 == "N/A" ? na : CrossoverType3 ? color_3 : color_4


WTVOB = wt1 >  60
WTVOS = wt1 < -60

// Weekness / Pos/Neg Pressure 

YellowWavePointingUp = YellowWave > YellowWave[1]

RSI14     = rsi(close, 14)
RSI14OB   = RSI14 > 70 ?     1 : 0
RSI14OS   = RSI14 < 30 ?     1 : 0 
RSI14OBOS = RSI14OB or RSI14OS ? 1 : 0

OBIndicatorsYellowPointingDown   = (RSI14OB or RSI14OB[1]) and WTVOB and not YellowWavePointingUp

OSIndicatorsYellowPointingUp     = (RSI14OS or RSI14OS[1]) and WTVOS and     YellowWavePointingUp


plot(PosNegPressure and OSIndicatorsYellowPointingUp ?      138.5      : na, "Wave Trend - Positive Pressure", color=color.new(#288a75, 25), style=plot.style_circles, linewidth=1)
plot(PosNegPressure and OBIndicatorsYellowPointingDown ?    138.5      : na, "Wave Trend - Negative Pressure", color=color.new(#DC143C, 32), style=plot.style_circles, linewidth=1)

alertcondition(OBIndicatorsYellowPointingDown or OSIndicatorsYellowPointingUp,      title=' -   Pos / Neg Pressure',  message='Pos / Neg Pressure - Trend Meter')


plot(TMSetups ?                                             134.5      : na, title = "All 3 Trend Meters Now Align", style=plot.style_circles, color=MSBar2Color, linewidth=3, transp=20)



plot(TMSetupsANDWT and ((PositiveWaveTrendCross and TrendBars3Positive) or (NegativeWaveTrendCross and TrendBars3Negative)) ?   134.5 : na, title="Wave Trend X & All 3 Trend Meters Now Align", style=plot.style_cross, color=MSBar2Color, linewidth=4, transp=20)



// Trend Barmeter Plots


plot(128.5, title="Trend Meter 1", style=plot.style_circles, color=TrendBar1Color, linewidth=2, transp=18)

plot(122.5, title="Trend Meter 2", style=plot.style_circles, color=TrendBar2Color, linewidth=2, transp=18)

plot(116.5, title="Trend Meter 3", style=plot.style_circles, color=TrendBar3Color, linewidth=2, transp=18)



plot(ShowTrendBar1 and     ShowTrendBar2 ? 110    : na, title="Trend Bar 1 - Thin Line",  style=plot.style_line, color=TrendBar4Color1, linewidth=4, transp=20)
plot(ShowTrendBar1 and not ShowTrendBar2 ? 110    : na, title="Trend Bar 1 - Thick Line", style=plot.style_line, color=TrendBar4Color1, linewidth=9, transp=20)

plot(ShowTrendBar2 and     ShowTrendBar1 ? 104.5  : na, title="Trend Bar 2 - Thin Line",  style=plot.style_line, color=TrendBar5Color1, linewidth=6, transp=20)
plot(ShowTrendBar2 and not ShowTrendBar1 ? 110    : na, title="Trend Bar 2 - Thick Line", style=plot.style_line, color=TrendBar5Color1, linewidth=9, transp=20)



// Background Highlights

TrendBar3BarsSame = TrendBars3Positive ? color.green : TrendBars3Negative ? color.red : na

TMa = hline(113.7, color=color.new(color.white, 100))

TMb = hline(131.3, color=color.new(color.white, 100))

fill(TMa, TMb, color=TrendBar3BarsSame, transp=91, title="Trend Meter Background Highlight - 3 Trend Meter Conditions Met")


// Alerts & Conditions - MA Crossing & Background Color


alertcondition(BackgroundColorChangePositive, title=' --  3 TMs Turn Green', message='All 3 Trend Meters Turn  Green - Trend Meter')
alertcondition(BackgroundColorChangeNegative, title=' --  3 TMs Turn Red',   message='All 3 Trend Meters Turn  Red - Trend Meter')
alertcondition(BackgroundColorChangePositive or BackgroundColorChangeNegative, title=' -- 3 TMs Change to Same Color', message='All 3 Trend Meters Change to Same Color - Trend Meter')


alertcondition(PositiveWaveTrendCross  and TrendBars3Positive, title="--- 3 TMs Turn Green & WaveTrend X", message='Green - Wave Trend Signal - Aligns with 3 Trend Meters - Trend Meter')
alertcondition(NegativeWaveTrendCross  and TrendBars3Negative, title="--- 3 TMs Turn Red & WaveTrend X",   message='Red - Wave Trend Signal - Aligns with 3 Trend Meters - Trend Meter')
alertcondition((PositiveWaveTrendCross and TrendBars3Positive) or (NegativeWaveTrendCross and TrendBars3Negative), title="--- 3 TMs Change to Same Color & WT X", message='Red / Green - Wave Trend Signal - Aligns with 3 Trend Meters - Trend Meter')



TrendMetersNoLongerAlign = ((not TrendBars3Positive or not TrendBars3Negative) and TrendBars3Positive[1]) or ((not TrendBars3Positive or not TrendBars3Negative) and TrendBars3Negative[1])

alertcondition(TrendMetersNoLongerAlign, title='---- 3 Trend Meters No Longer Align', message='3 Trend Meters No Longer Align - Trend Meter')


RapidColorChangePositive = TrendBars3Positive and (TrendBars3Negative[1] or TrendBars3Negative[2])
RapidColorChangeNegative = TrendBars3Negative and (TrendBars3Positive[1] or TrendBars3Positive[2])

alertcondition(RapidColorChangePositive, title='All 3 TMs Rapid Change Red to Green', message='All 3 Trend Meters Rapid Change Red to Green - Trend Meter')
alertcondition(RapidColorChangeNegative, title='All 3 TMs Rapid Change Green to Red', message='All 3 Trend Meters Rapid Change Green to Red - Trend Meter')
alertcondition(RapidColorChangePositive or RapidColorChangeNegative, title='All 3 TMs Rapid Change to Same Color', message='All 3 Trend Meters Rapid Change to Same Color - Trend Meter')


MaxValueMACrossUp   = crossover( ema(Close, 5), ema(Close, 11))
MaxValueMACrossDown = crossunder(ema(Close, 5), ema(Close, 11))


TB1MACrossUp   = crossover( MA1, MA2)
TB1MACrossDown = crossunder(MA1, MA2)


alertcondition(TB1MACrossUp,   title='TB 1 Turns Green', message='Trend Bar 1 - Turns Green - Trend Meter')
alertcondition(TB1MACrossDown, title='TB 1 Turns Red',   message='Trend Bar 1 - Turns Red - Trend Meter')
alertcondition(TB1MACrossUp or TB1MACrossDown, title='TB 1 Color Change',   message='Trend Bar 1 - Color Change - Trend Meter')


TB2MACrossUp   = crossover(MA3, MA4)
TB2MACrossDown = crossunder(MA3, MA4)


alertcondition(TB2MACrossUp,   title='TB 2 Turns Green', message='Trend Bar 2 - Turns Green - Trend Meter')
alertcondition(TB2MACrossDown, title='TB 2 Turns Red',   message='Trend Bar 2 - Turns Red - Trend Meter')
alertcondition(TB2MACrossUp or TB2MACrossDown, title='TB 2 Color Change',   message='Trend Bar 2 - Color Change - Trend Meter')


TB1Green  = MA1 > MA2
TB1Red    = MA1 < MA2

TB2Green  = MA3 > MA4
TB2Red    = MA3 < MA4

TB12Green = TB1Green and TB2Green and (TB1MACrossUp   or TB2MACrossUp)
TB12Red   = TB1Red   and TB2Red   and (TB1MACrossDown or TB2MACrossDown)

alertcondition(TB12Green,   title='TBs 1+2 Turn Green', message='Trend Bars 1+2 - Turn Green - Trend Meter')
alertcondition(TB12Red,     title='TBs 1+2 Turn Red',   message='Trend Bars 1+2 - Turn Red - Trend Meter')
alertcondition(TB12Green or TB12Red, title='TBs 1+2 Change to Same Color',   message='Trend Bars 1+2 - Change to Same Color - MAs Crossing - Trend Meter')


alertcondition(TB12Green  and TrendBars3Positive, title='TBs 1+2 Turn Green with 3 TMs', message='Trend Bars 1+2 - Turn Green with 3 TMs - Trend Meter')
alertcondition(TB12Red    and TrendBars3Negative, title='TBs 1+2 Turn Red with 3 TMs',   message='Trend Bars 1+2 - Turn Red with 3 TMs- Trend Meter')
alertcondition((TB12Green and TrendBars3Positive) or (TB12Red and TrendBars3Negative) ,  title='TBs 1+2 Change to Same Color with 3 TMs',   message='Trend Bars 1+2 - Change to Same Color with 3 TMs - Trend Meter')


alertcondition(TB1Green   and TrendBars3Positive, title='TB 1 Turns Green with 3 TMs',   message='Trend Bar 1 - Turn Green with 3 TMs - Trend Meter')
alertcondition(TB1Red     and TrendBars3Negative, title='TB 1 Turns Red with 3 TMs',     message='Trend Bar 1 - Turn Red with 3 TMs- Trend Meter')
alertcondition((TB1Green  and TrendBars3Positive) or (TB1Red and TrendBars3Negative) ,  title='TB 1 Change to Same Color with 3 TMs',       message='Trend Bar 1 - Change to Same Color with 3 TMs - Trend Meter')


alertcondition(TB2Green   and TrendBars3Positive, title='TB 2 Turns Green with 3 TMs',   message='Trend Bar 2 - Turn Green with 3 TMs - Trend Meter')
alertcondition(TB2Red     and TrendBars3Negative, title='TB 2 Turns Red with 3 TMs',     message='Trend Bar 2 - Turn Red with 3 TMs- Trend Meter')
alertcondition((TB2Green  and TrendBars3Positive) or (TB2Red and TrendBars3Negative) ,  title='TB 2 Change to Same Color with 3 TMs',       message='Trend Bar 2 - Change to Same Color with 3 TMs - Trend Meter')


alertcondition( BackgroundColorChangePositive  and TB1Green, title='3 TMs Turn Green with TB 1', message='All 3 Trend Meters Turn  Green with TB 1 - Trend Meter')
alertcondition( BackgroundColorChangeNegative  and TB1Red,   title='3 TMs Turn Red with TB 1',   message='All 3 Trend Meters Turn  Red with TB 1 - Trend Meter')
alertcondition((BackgroundColorChangePositive  and TB1Green) or (BackgroundColorChangeNegative and TB1Red), title='3 TMs Change Color with TB 1', message='All 3 Trend Meters Change Color with TB 1 - Trend Meter')


alertcondition( BackgroundColorChangePositive and TB2Green, title='3 TMs Turn Green with TB 2',  message='All 3 Trend Meters Turn  Green with TB 2 - Trend Meter')
alertcondition( BackgroundColorChangeNegative and TB2Red,   title='3 TMs Turn Red with TB 2',    message='All 3 Trend Meters Turn  Red with TB 2 - Trend Meter')
alertcondition((BackgroundColorChangePositive and TB2Green) or (BackgroundColorChangeNegative and TB2Red), title='3 TMs Change Color with TB 2',  message='All 3 Trend Meters Change Color with TB 2 - Trend Meter')


alertcondition( BackgroundColorChangePositive and TB1Green and TB2Green, title='3 TMs Turn Green with TBs 1+2', message='All 3 Trend Meters Turn  Green with Trend Bar 1+2 - Trend Meter')
alertcondition( BackgroundColorChangeNegative and TB1Red   and TB2Red,   title='3 TMs Turn Red with TBs 1+2',   message='All 3 Trend Meters Turn  Red with Trend Bar 1+2 - Trend Meter')
alertcondition((BackgroundColorChangePositive and TB1Green and TB2Green) or (BackgroundColorChangeNegative and TB1Red and TB2Red), title='3 TMs Change Color with TBs 1+2', message='All 3 Trend Meters Change Color with Trend Bar 1+2 - Trend Meter')


