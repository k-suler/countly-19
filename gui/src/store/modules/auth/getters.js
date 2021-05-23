import {auth} from "@/firebase/firebase";

export default {
  isAuthenticated() {
    return !!auth.currentUser;
  },
};
