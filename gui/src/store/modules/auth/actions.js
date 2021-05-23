import router from "@/router/index";
import * as fb from "@/firebase/firebase";
export default {
  logout() {
    fb.auth
      .signOut()
      .then(() => {
        router.push("/login");
      })
  },
  async login({ dispatch }, form) {
    await fb.auth.signInWithEmailAndPassword(
      form.email,
      form.password
    );
    await router.push("/stores");
  },
};
