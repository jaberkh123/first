from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client('b0c7a9c66ac3a6f4c4b809eb52f1430235ecb31b1ceadddf6669d9fad95fd278', '0d147ff33b2fdeae48e6594eeda0103c480b08c2ab4717fe48251876746222df',testnet=True)
#this is some code to do and some code
# get market depth
depth = client.get_order_book(symbol='BNBBTC')
