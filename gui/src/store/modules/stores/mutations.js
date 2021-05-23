export default {
  setStoreInfo(state, payload) {
    state.name = payload.name
    state.description = payload.name
    state.maxNumberOfCustomers = payload.name
    state.groundTruth = payload.name
    state.startTim = payload.name
  },
  setAllStores(state, payload){
    state.allStores = payload
  }
};
