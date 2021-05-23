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
    console.log(form);
    // sign user in
    const { user } = await fb.auth.signInWithEmailAndPassword(
      form.email,
      form.password
    );
    console.log(user);
    await router.push("/");
  },
};
