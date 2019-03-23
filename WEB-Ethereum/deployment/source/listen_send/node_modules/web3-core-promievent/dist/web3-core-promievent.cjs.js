'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

function _interopDefault (ex) { return (ex && (typeof ex === 'object') && 'default' in ex) ? ex['default'] : ex; }

var _classCallCheck = _interopDefault(require('@babel/runtime/helpers/classCallCheck'));
var _createClass = _interopDefault(require('@babel/runtime/helpers/createClass'));
var EventEmitter = _interopDefault(require('eventemitter3'));

var PromiEvent =
function () {
  function PromiEvent() {
    var _this = this;
    _classCallCheck(this, PromiEvent);
    this.promise = new Promise(function (resolve, reject) {
      _this.resolve = resolve;
      _this.reject = reject;
    });
    this.eventEmitter = new EventEmitter();
    return new Proxy(this, {
      get: this.proxyHandler
    });
  }
  _createClass(PromiEvent, [{
    key: "proxyHandler",
    value: function proxyHandler(target, name) {
      if (name === 'resolve' || name === 'reject') {
        return target[name];
      }
      if (name === 'then') {
        return target.promise.then.bind(target.promise);
      }
      if (name === 'catch') {
        return target.promise.catch.bind(target.promise);
      }
      if (target.eventEmitter[name]) {
        return target.eventEmitter[name];
      }
    }
  }]);
  return PromiEvent;
}();

exports.PromiEvent = PromiEvent;
