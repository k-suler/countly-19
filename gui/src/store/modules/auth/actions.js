import router from "@/router/index";
import * as fb from "@/firebase/firebase";
export default {
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
  async login({ dispatch }, form) {
    await fb.auth.signInWithEmailAndPassword(
      form.email,
      form.password
    );
    await router.push("/stores");
  },
};
