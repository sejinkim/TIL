class MonitorError(Exception):
    pass

class FeedError(MonitorError):      # 시세 수신 오류
    pass

class AlertError(MonitorError):     # 알림 처리 오류
    pass