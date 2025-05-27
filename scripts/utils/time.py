from datetime import datetime, time as dt_time
from pytz import timezone
from pandas.tseries.holiday import USFederalHolidayCalendar

def is_trading_time():
    now = datetime.now(timezone('US/Eastern'))
    
    # Check if it's a weekday
    if now.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        return False
    
    # Check if it's a holiday
    cal = USFederalHolidayCalendar()
    holidays = cal.holidays(start=now.date(), end=now.date())
    if now.date() in holidays:
        return False
    
    # Check if it's within market hours (9:30 AM to 4:00 PM Eastern Time)
    market_start = dt_time(9, 30)
    market_end = dt_time(16, 0)
    current_time = now.time()
    
    return market_start <= current_time <= market_end
