from bingX.perpetual.v2.types import (
    Order,
    PositionSide,
    Side,
)

def buyLong(bingx_client, symbol, betAmount, maxLev):
    bingx_client.trade.change_leverage(symbol=symbol, positionSide=PositionSide.LONG, leverage=maxLev)
    assetPrice = float(bingx_client.market.get_latest_price_of_trading_pair(symbol)['price'])
    
    Quanity = (betAmount * maxLev) / assetPrice

    # print(Quanity)
    # time.sleep(5)
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.BUY, positionSide=PositionSide.LONG, quantity=Quanity))
def closeLong(bingx_client, symbol, betAmount, maxLev):
    bingx_client.trade.change_leverage(symbol=symbol, positionSide=PositionSide.LONG, leverage=maxLev)
    assetPrice = float(bingx_client.market.get_latest_price_of_trading_pair(symbol)['price'])
    
    Quanity = (betAmount * maxLev) / assetPrice

    # print(Quanity)
    # time.sleep(5)
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.SELL, positionSide=PositionSide.LONG, quantity=Quanity))
def buyShort(bingx_client, symbol, betAmount, maxLev):
    bingx_client.trade.change_leverage(symbol=symbol, positionSide=PositionSide.LONG, leverage=maxLev)
    assetPrice = float(bingx_client.market.get_latest_price_of_trading_pair(symbol)['price'])
    
    Quanity = (betAmount * maxLev) / assetPrice

    # print(Quanity)
    # time.sleep(5)
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.SELL, positionSide=PositionSide.SHORT, quantity=Quanity))
def closeShort(bingx_client, symbol, betAmount, maxLev):
    bingx_client.trade.change_leverage(symbol=symbol, positionSide=PositionSide.LONG, leverage=maxLev)
    assetPrice = float(bingx_client.market.get_latest_price_of_trading_pair(symbol)['price'])
    
    Quanity = (betAmount * maxLev) / assetPrice

    # print(Quanity)
    # time.sleep(5)
    bingx_client.trade.create_order(Order(symbol=symbol, side=Side.BUY, positionSide=PositionSide.SHORT, quantity=Quanity))