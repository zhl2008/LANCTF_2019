import { Network } from 'web3-net';
import { ProvidersModuleFactory } from 'web3-providers';
import * as Utils from 'web3-utils';
import { formatters } from 'web3-core-helpers';
import { AbstractWeb3Module } from 'web3-core';
import { AbstractMethodFactory, GetAccountsMethod, NewAccountMethod, UnlockAccountMethod, LockAccountMethod, ImportRawKeyMethod, PersonalSendTransactionMethod, PersonalSignTransactionMethod, PersonalSignMethod, EcRecoverMethod, MethodModuleFactory } from 'web3-core-method';

class Personal extends AbstractWeb3Module {
  constructor(provider, providersModuleFactory, methodModuleFactory, methodFactory, net, utils, formatters$$1, options) {
    super(provider, providersModuleFactory, methodModuleFactory, methodFactory, options);
    this.utils = utils;
    this.formatters = formatters$$1;
    this.net = net;
  }
  setProvider(provider, net) {
    return !!(super.setProvider(provider, net) && this.net.setProvider(provider, net));
  }
  set defaultGasPrice(value) {
    super.defaultGasPrice = value;
    this.net.defaultGasPrice = value;
  }
  get defaultGasPrice() {
    return super.defaultGasPrice;
  }
  set defaultGas(value) {
    super.defaultGas = value;
    this.net.defaultGas = value;
  }
  get defaultGas() {
    return super.defaultGas;
  }
  set transactionBlockTimeout(value) {
    super.transactionBlockTimeout = value;
    this.net.transactionBlockTimeout = value;
  }
  get transactionBlockTimeout() {
    return super.transactionBlockTimeout;
  }
  set transactionConfirmationBlocks(value) {
    super.transactionConfirmationBlocks = value;
    this.net.transactionConfirmationBlocks = value;
  }
  get transactionConfirmationBlocks() {
    return super.transactionConfirmationBlocks;
  }
  set transactionPollingTimeout(value) {
    super.transactionPollingTimeout = value;
    this.net.transactionPollingTimeout = value;
  }
  get transactionPollingTimeout() {
    return super.transactionPollingTimeout;
  }
  set defaultAccount(value) {
    super.defaultAccount = value;
    this.net.defaultAccount = value;
  }
  get defaultAccount() {
    return super.defaultAccount;
  }
  set defaultBlock(value) {
    super.defaultBlock = value;
    this.net.defaultBlock = value;
  }
  get defaultBlock() {
    return super.defaultBlock;
  }
}

class MethodFactory extends AbstractMethodFactory {
  constructor(methodModuleFactory, utils, formatters$$1) {
    super(methodModuleFactory, utils, formatters$$1);
    this.methods = {
      getAccounts: GetAccountsMethod,
      newAccount: NewAccountMethod,
      unlockAccount: UnlockAccountMethod,
      lockAccount: LockAccountMethod,
      importRawKey: ImportRawKeyMethod,
      sendTransaction: PersonalSendTransactionMethod,
      signTransaction: PersonalSignTransactionMethod,
      sign: PersonalSignMethod,
      ecRecover: EcRecoverMethod
    };
  }
}

class PersonalModuleFactory {
  constructor(utils, formatters$$1) {
    this.utils = utils;
    this.formatters = formatters$$1;
  }
  createPersonalModule(provider, providersModuleFactory, methodModuleFactory, net, options) {
    return new Personal(provider, providersModuleFactory, methodModuleFactory, this.createMethodFactory(methodModuleFactory), net, this.utils, this.formatters, options);
  }
  createMethodFactory(methodModuleFactory) {
    return new MethodFactory(methodModuleFactory, this.utils, this.formatters);
  }
}

const Personal$1 = (provider, accounts, options) => {
  return new PersonalModuleFactory(Utils, formatters).createPersonalModule(provider, new ProvidersModuleFactory(), new MethodModuleFactory(accounts), new Network(provider, options), options);
};

export { Personal$1 as Personal };
