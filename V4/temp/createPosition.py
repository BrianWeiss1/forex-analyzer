from bingX.perpetual.v2.types import (
    Order,
    PositionSide,
    Side,
    OrderType,
)
from bingX.perpetual.v2 import PerpetualV2


def buyLong(bingx_client: PerpetualV2, symbol, betAmount, maxLev, stopLossAmount):
    bingx_client.trade.change_leverage(symbol=symbol, positionSide=PositionSide.LONG, leverage=maxLev)
    assetPrice = float(bingx_client.market.get_latest_price_of_trading_pair(symbol)['price'])
    
    Quanity = round((betAmount * maxLev) / assetPrice, 6)
    StopLoss = assetPrice * (1-(stopLossAmount / maxLev))
    
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.BUY, positionSide=PositionSide.LONG, quantity=Quanity, type=OrderType.MARKET, stopPrice=StopLoss))
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.BUY, positionSide=PositionSide.LONG, quantity=Quanity, type=OrderType.STOP_MARKET, stopPrice=StopLoss))
def closeLong(bingx_client, symbol, betAmount, maxLev):
    bingx_client.trade.change_leverage(symbol=symbol, positionSide=PositionSide.LONG, leverage=maxLev)
    assetPrice = float(bingx_client.market.get_latest_price_of_trading_pair(symbol)['price'])
    
    Quanity = round((betAmount * maxLev) / assetPrice, 6)

    # print(Quanity)
    # time.sleep(5)
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.SELL, positionSide=PositionSide.LONG, quantity=Quanity))
def buyShort(bingx_client, symbol, betAmount, maxLev, stopLossAmount):
    bingx_client.trade.change_leverage(symbol=symbol, positionSide=PositionSide.LONG, leverage=maxLev)
    assetPrice = float(bingx_client.market.get_latest_price_of_trading_pair(symbol)['price'])
    
    Quanity = round((betAmount * maxLev) / assetPrice, 6)
    print(Quanity)
    StopLoss = assetPrice * (1+(stopLossAmount / maxLev))
    
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.SELL, positionSide=PositionSide.SHORT, quantity=Quanity, type=OrderType.MARKET, stopPrice=StopLoss))
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.SELL, positionSide=PositionSide.SHORT, quantity=Quanity, type=OrderType.STOP_MARKET, stopPrice=StopLoss))
def closeShort(bingx_client, symbol, betAmount, maxLev):
    bingx_client.trade.change_leverage(symbol=symbol, positionSide=PositionSide.LONG, leverage=maxLev)
    assetPrice = float(bingx_client.market.get_latest_price_of_trading_pair(symbol)['price'])
    
    Quanity = round((betAmount * maxLev) / assetPrice, 6)

    # print(Quanity)
    # time.sleep(5)
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.BUY, positionSide=PositionSide.SHORT, quantity=Quanity))
    
                # Trade.change_leverage() got an unexpected keyword argument 'positionSide'
