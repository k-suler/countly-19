export default {
  async registerStore(context, data) {
    const userId = context.rootGetters.userId;
    const storeData = {
      name: data.first,
      description: data.last,
      maxNumberOfCustomers: data.desc,
    };

    const token = context.rootGetters.token;

    const response = await fetch(
      `https://countly-19-default-rtdb.europe-west1.firebasedatabase.app/stores/${userId}.json?auth=` +
        token,
      {
        method: "PUT",
        body: JSON.stringify(storeData),
      }
    );

    // const responseData = await response.json();

    if (!response.ok) {
      // error ...
    }

    context.commit("registerStore", {
      ...storeData,
      id: userId,
    });
  },
  async loadCoaches(context) {
    const response = await fetch(
      `https://countly-19-default-rtdb.europe-west1.firebasedatabase.app/stores.json`
    );
    const responseData = await response.json();

    if (!response.ok) {
      const error = new Error(responseData.message || "Failed to fetch!");
      throw error;
    }

    const stores = [];

    for (const key in responseData) {
      const store = {
        id: key,
        name: responseData[key].name,
        maxNumberOfCustomers: responseData[key].maxNumberOfCustomers,
        description: responseData[key].description,
      };
      stores.push(store);
    }

    context.commit("setStores", stores);
    context.commit("setFetchTimestamp");
  },
};
