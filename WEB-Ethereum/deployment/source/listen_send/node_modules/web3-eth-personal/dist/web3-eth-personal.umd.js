(function (global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports, require('web3-net'), require('web3-providers'), require('web3-utils'), require('web3-core-helpers'), require('@babel/runtime/helpers/createClass'), require('@babel/runtime/helpers/set'), require('@babel/runtime/helpers/get'), require('web3-core'), require('@babel/runtime/helpers/classCallCheck'), require('@babel/runtime/helpers/possibleConstructorReturn'), require('@babel/runtime/helpers/getPrototypeOf'), require('@babel/runtime/helpers/inherits'), require('web3-core-method')) :
    typeof define === 'function' && define.amd ? define(['exports', 'web3-net', 'web3-providers', 'web3-utils', 'web3-core-helpers', '@babel/runtime/helpers/createClass', '@babel/runtime/helpers/set', '@babel/runtime/helpers/get', 'web3-core', '@babel/runtime/helpers/classCallCheck', '@babel/runtime/helpers/possibleConstructorReturn', '@babel/runtime/helpers/getPrototypeOf', '@babel/runtime/helpers/inherits', 'web3-core-method'], factory) :
    (factory((global.Web3EthPersonal = {}),global.web3Net,global.web3Providers,global.Utils,global.web3CoreHelpers,global._createClass,global._set,global._get,global.web3Core,global._classCallCheck,global._possibleConstructorReturn,global._getPrototypeOf,global._inherits,global.web3CoreMethod));
}(this, (function (exports,web3Net,web3Providers,Utils,web3CoreHelpers,_createClass,_set,_get,web3Core,_classCallCheck,_possibleConstructorReturn,_getPrototypeOf,_inherits,web3CoreMethod) { 'use strict';

    _createClass = _createClass && _createClass.hasOwnProperty('default') ? _createClass['default'] : _createClass;
    _set = _set && _set.hasOwnProperty('default') ? _set['default'] : _set;
    _get = _get && _get.hasOwnProperty('default') ? _get['default'] : _get;
    _classCallCheck = _classCallCheck && _classCallCheck.hasOwnProperty('default') ? _classCallCheck['default'] : _classCallCheck;
    _possibleConstructorReturn = _possibleConstructorReturn && _possibleConstructorReturn.hasOwnProperty('default') ? _possibleConstructorReturn['default'] : _possibleConstructorReturn;
    _getPrototypeOf = _getPrototypeOf && _getPrototypeOf.hasOwnProperty('default') ? _getPrototypeOf['default'] : _getPrototypeOf;
    _inherits = _inherits && _inherits.hasOwnProperty('default') ? _inherits['default'] : _inherits;

    var Personal =
    function (_AbstractWeb3Module) {
      _inherits(Personal, _AbstractWeb3Module);
      function Personal(provider, providersModuleFactory, methodModuleFactory, methodFactory, net, utils, formatters, options) {
        var _this;
        _classCallCheck(this, Personal);
        _this = _possibleConstructorReturn(this, _getPrototypeOf(Personal).call(this, provider, providersModuleFactory, methodModuleFactory, methodFactory, options));
        _this.utils = utils;
        _this.formatters = formatters;
        _this.net = net;
        return _this;
      }
      _createClass(Personal, [{
        key: "setProvider",
        value: function setProvider(provider, net) {
          return !!(_get(_getPrototypeOf(Personal.prototype), "setProvider", this).call(this, provider, net) && this.net.setProvider(provider, net));
        }
      }, {
        key: "defaultGasPrice",
        set: function set(value) {
          _set(_getPrototypeOf(Personal.prototype), "defaultGasPrice", value, this, true);
          this.net.defaultGasPrice = value;
        }
        ,
        get: function get() {
          return _get(_getPrototypeOf(Personal.prototype), "defaultGasPrice", this);
        }
      }, {
        key: "defaultGas",
        set: function set(value) {
          _set(_getPrototypeOf(Personal.prototype), "defaultGas", value, this, true);
          this.net.defaultGas = value;
        }
        ,
        get: function get() {
          return _get(_getPrototypeOf(Personal.prototype), "defaultGas", this);
        }
      }, {
        key: "transactionBlockTimeout",
        set: function set(value) {
          _set(_getPrototypeOf(Personal.prototype), "transactionBlockTimeout", value, this, true);
          this.net.transactionBlockTimeout = value;
        }
        ,
        get: function get() {
          return _get(_getPrototypeOf(Personal.prototype), "transactionBlockTimeout", this);
        }
      }, {
        key: "transactionConfirmationBlocks",
        set: function set(value) {
          _set(_getPrototypeOf(Personal.prototype), "transactionConfirmationBlocks", value, this, true);
          this.net.transactionConfirmationBlocks = value;
        }
        ,
        get: function get() {
          return _get(_getPrototypeOf(Personal.prototype), "transactionConfirmationBlocks", this);
        }
      }, {
        key: "transactionPollingTimeout",
        set: function set(value) {
          _set(_getPrototypeOf(Personal.prototype), "transactionPollingTimeout", value, this, true);
          this.net.transactionPollingTimeout = value;
        }
        ,
        get: function get() {
          return _get(_getPrototypeOf(Personal.prototype), "transactionPollingTimeout", this);
        }
      }, {
        key: "defaultAccount",
        set: function set(value) {
          _set(_getPrototypeOf(Personal.prototype), "defaultAccount", value, this, true);
          this.net.defaultAccount = value;
        }
        ,
        get: function get() {
          return _get(_getPrototypeOf(Personal.prototype), "defaultAccount", this);
        }
      }, {
        key: "defaultBlock",
        set: function set(value) {
          _set(_getPrototypeOf(Personal.prototype), "defaultBlock", value, this, true);
          this.net.defaultBlock = value;
        }
        ,
        get: function get() {
          return _get(_getPrototypeOf(Personal.prototype), "defaultBlock", this);
        }
      }]);
      return Personal;
    }(web3Core.AbstractWeb3Module);

    var MethodFactory =
    function (_AbstractMethodFactor) {
      _inherits(MethodFactory, _AbstractMethodFactor);
      function MethodFactory(methodModuleFactory, utils, formatters) {
        var _this;
        _classCallCheck(this, MethodFactory);
        _this = _possibleConstructorReturn(this, _getPrototypeOf(MethodFactory).call(this, methodModuleFactory, utils, formatters));
        _this.methods = {
          getAccounts: web3CoreMethod.GetAccountsMethod,
          newAccount: web3CoreMethod.NewAccountMethod,
          unlockAccount: web3CoreMethod.UnlockAccountMethod,
          lockAccount: web3CoreMethod.LockAccountMethod,
          importRawKey: web3CoreMethod.ImportRawKeyMethod,
          sendTransaction: web3CoreMethod.PersonalSendTransactionMethod,
          signTransaction: web3CoreMethod.PersonalSignTransactionMethod,
          sign: web3CoreMethod.PersonalSignMethod,
          ecRecover: web3CoreMethod.EcRecoverMethod
        };
        return _this;
      }
      return MethodFactory;
    }(web3CoreMethod.AbstractMethodFactory);

    var PersonalModuleFactory =
    function () {
      function PersonalModuleFactory(utils, formatters) {
        _classCallCheck(this, PersonalModuleFactory);
        this.utils = utils;
        this.formatters = formatters;
      }
      _createClass(PersonalModuleFactory, [{
        key: "createPersonalModule",
        value: function createPersonalModule(provider, providersModuleFactory, methodModuleFactory, net, options) {
          return new Personal(provider, providersModuleFactory, methodModuleFactory, this.createMethodFactory(methodModuleFactory), net, this.utils, this.formatters, options);
        }
      }, {
        key: "createMethodFactory",
        value: function createMethodFactory(methodModuleFactory) {
          return new MethodFactory(methodModuleFactory, this.utils, this.formatters);
        }
      }]);
      return PersonalModuleFactory;
    }();

    var Personal$1 = function Personal(provider, accounts, options) {
      return new PersonalModuleFactory(Utils, web3CoreHelpers.formatters).createPersonalModule(provider, new web3Providers.ProvidersModuleFactory(), new web3CoreMethod.MethodModuleFactory(accounts), new web3Net.Network(provider, options), options);
    };

    exports.Personal = Personal$1;

    Object.defineProperty(exports, '__esModule', { value: true });

})));
