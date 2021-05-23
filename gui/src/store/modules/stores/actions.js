import {storesCollection} from "@/firebase/firebase";

export default {
    async fetchStoreData({ commit }, storeId) {
        storesCollection
            .doc(`${storeId}`)
            .get()
            .then((res) => {
                commit("setStoreInfo", res.data())
            });
    },
    async fetchAllStores({commit}){
        const stores = [];
        (await storesCollection
            .get())
            .forEach(doc => {
                stores.push({"storeId": doc.ref.id, ...doc.data()})
            })
        commit("setAllStores", stores)
    }
};
