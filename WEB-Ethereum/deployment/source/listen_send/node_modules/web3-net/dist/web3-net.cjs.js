'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

function _interopDefault (ex) { return (ex && (typeof ex === 'object') && 'default' in ex) ? ex['default'] : ex; }

var web3Providers = require('web3-providers');
var web3CoreHelpers = require('web3-core-helpers');
var Utils = require('web3-utils');
var _regeneratorRuntime = _interopDefault(require('@babel/runtime/regenerator'));
var _asyncToGenerator = _interopDefault(require('@babel/runtime/helpers/asyncToGenerator'));
var _createClass = _interopDefault(require('@babel/runtime/helpers/createClass'));
var web3Core = require('web3-core');
var isFunction = _interopDefault(require('lodash/isFunction'));
var _classCallCheck = _interopDefault(require('@babel/runtime/helpers/classCallCheck'));
var _possibleConstructorReturn = _interopDefault(require('@babel/runtime/helpers/possibleConstructorReturn'));
var _getPrototypeOf = _interopDefault(require('@babel/runtime/helpers/getPrototypeOf'));
var _inherits = _interopDefault(require('@babel/runtime/helpers/inherits'));
var web3CoreMethod = require('web3-core-method');

var Network =
function (_AbstractWeb3Module) {
  _inherits(Network, _AbstractWeb3Module);
  function Network(provider, providersModuleFactory, methodModuleFactory, methodFactory, utils, formatters, options) {
    var _this;
    _classCallCheck(this, Network);
    _this = _possibleConstructorReturn(this, _getPrototypeOf(Network).call(this, provider, providersModuleFactory, methodModuleFactory, methodFactory, options));
    _this.utils = utils;
    _this.formatters = formatters;
    return _this;
  }
  _createClass(Network, [{
    key: "getNetworkType",
    value: function () {
      var _getNetworkType = _asyncToGenerator(
      _regeneratorRuntime.mark(function _callee(callback) {
        var id, genesisBlock, returnValue;
        return _regeneratorRuntime.wrap(function _callee$(_context) {
          while (1) {
            switch (_context.prev = _context.next) {
              case 0:
                _context.prev = 0;
                _context.next = 3;
                return this.getId();
              case 3:
                id = _context.sent;
                _context.next = 6;
                return this.getBlock(0, false);
              case 6:
                genesisBlock = _context.sent;
                returnValue = 'private';
                if (genesisBlock.hash === '0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3' && id === 1) {
                  returnValue = 'main';
                }
                if (genesisBlock.hash === '0cd786a2425d16f152c658316c423e6ce1181e15c3295826d7c9904cba9ce303' && id === 2) {
                  returnValue = 'morden';
                }
                if (genesisBlock.hash === '0x41941023680923e0fe4d74a34bdac8141f2540e3ae90623718e47d66d1ca4a2d' && id === 3) {
                  returnValue = 'ropsten';
                }
                if (genesisBlock.hash === '0x6341fd3daf94b748c72ced5a5b26028f2474f5f00d824504e4fa37a75767e177' && id === 4) {
                  returnValue = 'rinkeby';
                }
                if (genesisBlock.hash === '0xa3c565fc15c7478862d50ccd6561e3c06b24cc509bf388941c25ea985ce32cb9' && id === 42) {
                  returnValue = 'kovan';
                }
                if (isFunction(callback)) {
                  callback(null, returnValue);
                }
                return _context.abrupt("return", returnValue);
              case 17:
                _context.prev = 17;
                _context.t0 = _context["catch"](0);
                if (isFunction(callback)) {
                  callback(_context.t0, null);
                }
                throw _context.t0;
              case 21:
              case "end":
                return _context.stop();
            }
          }
        }, _callee, this, [[0, 17]]);
      }));
      return function getNetworkType(_x) {
        return _getNetworkType.apply(this, arguments);
      };
    }()
  }]);
  return Network;
}(web3Core.AbstractWeb3Module);

var MethodFactory =
function (_AbstractMethodFactor) {
  _inherits(MethodFactory, _AbstractMethodFactor);
  function MethodFactory(methodModuleFactory, utils, formatters) {
    var _this;
    _classCallCheck(this, MethodFactory);
    _this = _possibleConstructorReturn(this, _getPrototypeOf(MethodFactory).call(this, methodModuleFactory, utils, formatters));
    _this.methods = {
      getId: web3CoreMethod.VersionMethod,
      getBlock: web3CoreMethod.GetBlockMethod,
      isListening: web3CoreMethod.ListeningMethod,
      getPeerCount: web3CoreMethod.PeerCountMethod
    };
    return _this;
  }
  return MethodFactory;
}(web3CoreMethod.AbstractMethodFactory);

var NetworkModuleFactory =
function () {
  function NetworkModuleFactory(utils, formatters) {
    _classCallCheck(this, NetworkModuleFactory);
    this.utils = utils;
    this.formatters = formatters;
  }
  _createClass(NetworkModuleFactory, [{
    key: "createNetworkModule",
    value: function createNetworkModule(provider, providersModuleFactory, methodModuleFactory, options) {
      return new Network(provider, providersModuleFactory, methodModuleFactory, this.createMethodFactory(methodModuleFactory), this.utils, this.formatters, options);
    }
  }, {
    key: "createMethodFactory",
    value: function createMethodFactory(methodModuleFactory) {
      return new MethodFactory(methodModuleFactory, this.utils, this.formatters);
    }
  }]);
  return NetworkModuleFactory;
}();

var Network$1 = function Network(provider, options) {
  return new NetworkModuleFactory(Utils, web3CoreHelpers.formatters).createNetworkModule(provider, new web3Providers.ProvidersModuleFactory(), new web3CoreMethod.MethodModuleFactory(), options);
};

exports.Network = Network$1;
