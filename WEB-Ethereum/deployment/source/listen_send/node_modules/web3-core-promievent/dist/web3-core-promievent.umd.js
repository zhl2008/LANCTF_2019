(function (global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports, require('@babel/runtime/helpers/classCallCheck'), require('@babel/runtime/helpers/createClass'), require('eventemitter3')) :
    typeof define === 'function' && define.amd ? define(['exports', '@babel/runtime/helpers/classCallCheck', '@babel/runtime/helpers/createClass', 'eventemitter3'], factory) :
    (factory((global.Web3CorePromiEvent = {}),global._classCallCheck,global._createClass,global.EventEmitter));
}(this, (function (exports,_classCallCheck,_createClass,EventEmitter) { 'use strict';

    _classCallCheck = _classCallCheck && _classCallCheck.hasOwnProperty('default') ? _classCallCheck['default'] : _classCallCheck;
    _createClass = _createClass && _createClass.hasOwnProperty('default') ? _createClass['default'] : _createClass;
    EventEmitter = EventEmitter && EventEmitter.hasOwnProperty('default') ? EventEmitter['default'] : EventEmitter;

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

    Object.defineProperty(exports, '__esModule', { value: true });

})));
