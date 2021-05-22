
export default {
  updateMaxValueOfPeople(context, payload) {
    // TODO set url
    let url =
        "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyD3Q1oHXOFNtRB7vxu63rtQk8aI18oUSg4";
    const response = fetch(url, {
      method: "GET",
      body: JSON.stringify({
        storeId: payload.storeId,
      }),
    });
    const responseData = response.json();
    if (!response.ok) {
      const error = new Error(
          responseData.message || "Failed to fetch data."
      );
      throw error;
    }
    context.commit("setMaxNumOfPeople", {
      maxNumOfPeople: responseData.maxNumOfPeople,

    });


  },
  updateCurrentCounter(context, payload) {
  // TODO set url
    let url =
        "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyD3Q1oHXOFNtRB7vxu63rtQk8aI18oUSg4";
    const response = fetch(url, {
      method: "GET",
      body: JSON.stringify({
        storeId: payload.storeId,
      }),
    });
    const responseData = response.json();
    if (!response.ok) {
      const error = new Error(
          responseData.message || "Failed to fetch data."
      );
      throw error;
    }
    context.commit("setCurrentNumCount", {
      currentNumPeople: responseData.currentNumPeople,
    })
  }
};
