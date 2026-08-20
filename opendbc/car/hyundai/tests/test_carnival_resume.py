from opendbc.car.hyundai.carcontroller import should_send_canfd_resume


def test_carnival_resume_continues_while_request_is_active_after_five_seconds():
  # Route b3344051f4d069e6|00000001--6534eefb84 has a 6.349-second
  # legitimate factory-SCC resume request. The RES press must not expire at
  # the previous five-second cap while that request remains active.
  assert not should_send_canfd_resume(False, False, 1)
  assert should_send_canfd_resume(False, False, 2)
  assert should_send_canfd_resume(True, False, 0)
  assert should_send_canfd_resume(False, True, 0)
