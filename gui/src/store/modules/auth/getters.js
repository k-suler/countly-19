import {auth} from "@/firebase/firebase";

export default {
  userId(state) {
    return state.userId;
  },
  userEmail(state) {
    return state.email;
  },
  token(state) {
    return state.token;
  },
  isAuthenticated(state) {
    return !!auth.currentUser;
  },
  didAutoLogout(state) {
    return state.didAutoLogout;
  },
};
