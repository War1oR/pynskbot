from tornado.ioloop import PeriodicCallback as PC

__author__ = 'warior'
__date__ = '28.10.2015'


class PeriodicCallback(PC):

    def __init__(self, callback, arg, callback_time, io_loop=None):
        super(PeriodicCallback, self).__init__(callback, callback_time, io_loop)
        self.arg = arg

    def _run(self):
        if not self._running:
            return
        try:
            return self.callback(self.arg)
        except Exception:
            self.io_loop.handle_callback_exception(self.callback)
        finally:
            self._schedule_next()