import router from "@/router/index";
import * as fb from "@/firebase/firebase";
import { storesCollection } from "@/firebase/firebase";
export default {
  // async login(context, payload) {
  //   return context.dispatch("auth", {
  //     ...payload,
  //     mode: "login",
  //   });
  // },
  //
  // async signup(context, payload) {
  //   return context.dispatch("auth", {
  //     ...payload,
  //     mode: "signup",
  //   });
  // },
  // async auth(context, payload) {
  //   const mode = payload.mode;
  //   let url =
  //     "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyD3Q1oHXOFNtRB7vxu63rtQk8aI18oUSg4";
  //
  //   if (mode === "signup") {
  //     url =
  //       "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyD3Q1oHXOFNtRB7vxu63rtQk8aI18oUSg4";
  //   }
  //   const response = await fetch(url, {
  //     method: "POST",
  //     body: JSON.stringify({
  //       email: payload.email,
  //       password: payload.password,
  //       returnSecureToken: true,
  //     }),
  //   });
  //
  //   const responseData = await response.json();
  //
  //   if (!response.ok) {
  //     const error = new Error(
  //       responseData.message || "Failed to authenticate. Check your login data."
  //     );
  //     throw error;
  //   }
  //
  //   const expiresIn = +responseData.expiresIn * 1000;
  //   // const expiresIn = 5000;
  //   const expirationDate = new Date().getTime() + expiresIn;
  //
  //   localStorage.setItem("token", responseData.idToken);
  //   localStorage.setItem("userId", responseData.localId);
  //   localStorage.setItem("tokenExpiration", expirationDate);
  //
  //   timer = setTimeout(function () {
  //     context.dispatch("autoLogout");
  //   }, expiresIn);
  //
  //   context.commit("setUser", {
  //     token: responseData.idToken,
  //     userId: responseData.localId,
  //   });
  //   router.replace("/");
  // },
  // tryLogin(context) {
  //   const token = localStorage.getItem("token");
  //   const userId = localStorage.getItem("userId");
  //   const tokenExpiration = localStorage.getItem("tokenExpiration");
  //
  //   const expiresIn = +tokenExpiration - new Date().getTime();
  //
  //   if (expiresIn < 0) {
  //     return;
  //   }
  //
  //   timer = setTimeout(function () {
  //     context.dispatch("autoLogout");
  //   }, expiresIn);
  //
  //   if (token && userId) {
  //     context.commit("setUser", {
  //       token: token,
  //       userId: userId,
  //     });
  //   }
  // },
  logout(context) {
    fb.auth
      .signOut()
      .then(() => {
        // Sign-out successful.
        router.push("/login");
      })
      .catch((error) => {
        // An error happened.
      });
  },
  // autoLogout(context) {
  //   context.dispatch("logout");
  //   context.commit("setAutoLogout");
  // },

  async login({ dispatch }, form) {
    console.log(form);
    // sign user in
    const { user } = await fb.auth.signInWithEmailAndPassword(
      form.email,
      form.password
    );
    console.log(user);
    await router.push("/");
  },
  async fetStoreData({ commit }, storeId) {
    storesCollection
      .doc(`${storeId}`)
      .get()
      .then((res) => {
        console.log(res.data());
      });
  },
};
