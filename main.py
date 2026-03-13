
import time
import market_data
import strategy_engine
import telegram_bot
import logger
import signal_manager
import stats_engine

ASSETS = ["crudeoil"]

def run():

    logger.log("ELITE BOT CRUDE OIL STARTED")

    while True:

        for asset in ASSETS:

            df = market_data.get_data(asset)

            if df is None:
                logger.log(f"No data for {asset}")
                continue

            signal = strategy_engine.analyze_market(df,asset)

            if signal:

                if signal_manager.can_send_signal():

                    signal_manager.register_signal(signal)
                    stats_engine.record_signal(signal)

                    telegram_bot.send_signal(signal)

                    logger.log(f"Signal sent {signal['asset']} score {signal['score']}")

        time.sleep(60)


if __name__ == "__main__":
    run()
