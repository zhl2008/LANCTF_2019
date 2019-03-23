import { ProvidersModuleFactory } from 'web3-providers';
import { formatters } from 'web3-core-helpers';
import * as Utils from 'web3-utils';
import { AbstractWeb3Module } from 'web3-core';
import isFunction from 'lodash/isFunction';
import { AbstractMethodFactory, GetBlockMethod, ListeningMethod, PeerCountMethod, VersionMethod, MethodModuleFactory } from 'web3-core-method';

class Network extends AbstractWeb3Module {
  constructor(provider, providersModuleFactory, methodModuleFactory, methodFactory, utils, formatters$$1, options) {
    super(provider, providersModuleFactory, methodModuleFactory, methodFactory, options);
    this.utils = utils;
    this.formatters = formatters$$1;
  }
  async getNetworkType(callback) {
    try {
      const id = await this.getId();
      const genesisBlock = await this.getBlock(0, false);
      let returnValue = 'private';
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
      return returnValue;
    } catch (error) {
      if (isFunction(callback)) {
        callback(error, null);
      }
      throw error;
    }
  }
}

class MethodFactory extends AbstractMethodFactory {
  constructor(methodModuleFactory, utils, formatters$$1) {
    super(methodModuleFactory, utils, formatters$$1);
    this.methods = {
      getId: VersionMethod,
      getBlock: GetBlockMethod,
      isListening: ListeningMethod,
      getPeerCount: PeerCountMethod
    };
  }
}

class NetworkModuleFactory {
  constructor(utils, formatters$$1) {
    this.utils = utils;
    this.formatters = formatters$$1;
  }
  createNetworkModule(provider, providersModuleFactory, methodModuleFactory, options) {
    return new Network(provider, providersModuleFactory, methodModuleFactory, this.createMethodFactory(methodModuleFactory), this.utils, this.formatters, options);
  }
  createMethodFactory(methodModuleFactory) {
    return new MethodFactory(methodModuleFactory, this.utils, this.formatters);
  }
}

const Network$1 = (provider, options) => {
  return new NetworkModuleFactory(Utils, formatters).createNetworkModule(provider, new ProvidersModuleFactory(), new MethodModuleFactory(), options);
};

export { Network$1 as Network };
