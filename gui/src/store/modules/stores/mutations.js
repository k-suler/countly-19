export default {
  registerStore(state, payload) {
    state.stores.push(payload);
  },
  setStore(state, payload) {
    state.stores = payload;
  },
  setFetchTimestamp(state) {
    state.lastFetch = new Date().getTime();
  },
};
