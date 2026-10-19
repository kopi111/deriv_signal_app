"""Where alerts go: Firebase Cloud Messaging, or the console for dry runs."""


def price(value):
    if abs(value) < 10:
        return f"{value:.5f}"
    if abs(value) < 1000:
        return f"{value:.3f}"
    return f"{value:.2f}"


def headline(signal):
    return f"{signal.direction} {signal.name}"


def detail(signal):
    caution = "" if signal.proven else " Unproven setup, trade small."
    return (f"Entry {price(signal.entry)}, SL {price(signal.stop)}, "
            f"TP {price(signal.target)}.{caution}")


class ConsoleNotifier:
    def send(self, signal):
        print(f"[alert] {headline(signal)}: {detail(signal)}", flush=True)


class FcmNotifier:
    """Sends to an FCM topic that every installed copy of the app subscribes to."""

    def __init__(self, service_account_path, topic):
        import firebase_admin
        from firebase_admin import credentials, messaging
        self._messaging = messaging
        self._topic = topic
        firebase_admin.initialize_app(credentials.Certificate(service_account_path))

    def send(self, signal):
        message = self._messaging.Message(
            topic=self._topic,
            notification=self._messaging.Notification(title=headline(signal), body=detail(signal)),
            data={"symbol": signal.symbol, "direction": signal.direction,
                  "entry": str(signal.entry), "stop": str(signal.stop),
                  "target": str(signal.target), "candle_epoch": str(signal.candle_epoch)},
            android=self._messaging.AndroidConfig(priority="high"),
        )
        self._messaging.send(message)
        print(f"[pushed] {headline(signal)}: {detail(signal)}", flush=True)
