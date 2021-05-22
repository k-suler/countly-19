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
    return !!state.token;
  },
  didAutoLogout(state) {
    return state.didAutoLogout;
  },
};
