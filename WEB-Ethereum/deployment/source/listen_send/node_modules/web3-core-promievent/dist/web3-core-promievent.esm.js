import EventEmitter from 'eventemitter3';

class PromiEvent {
  constructor() {
    this.promise = new Promise((resolve, reject) => {
      this.resolve = resolve;
      this.reject = reject;
    });
    this.eventEmitter = new EventEmitter();
    return new Proxy(this, {
      get: this.proxyHandler
    });
  }
  proxyHandler(target, name) {
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
}

export { PromiEvent };
