<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md6>
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title style="color: #010101">Login</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                prepend-icon="mdi-account"
                v-model="formData.email"
                name="login"
                label="Email address"
                type="text"
              ></v-text-field>
              <v-text-field
                prepend-icon="mdi-lock"
                v-model="formData.password"
                name="password"
                label="Password"
                id="password"
                type="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="login(formData)" style="color: #010101" block>
              Login &nbsp;
              <v-icon class="ml-3">mdi-send</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import { mapActions } from "vuex";

export default {
  data: () => ({
    formData: {
      email: null,
      password: null
    }
  }),
  methods: {
    ...mapActions("auth", ["login", "logout"])
  }
};
</script>

<style scoped></style>
