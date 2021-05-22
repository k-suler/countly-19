<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md6>
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Registracija</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                prepend-icon="mdi-account"
                name="login"
                v-model="formData.username"
                label="Uporabniško ime"
                type="text"
              ></v-text-field>
              <v-text-field
                prepend-icon="mdi-email"
                name="login"
                v-model="formData.email"
                label="Email"
                type="text"
              ></v-text-field>
              <v-text-field
                prepend-icon="mdi-lock"
                name="password"
                v-model="formData.password"
                label="Geslo"
                id="password"
                type="password"
              ></v-text-field>
              <v-text-field
                prepend-icon="mdi-lock"
                name="password"
                label="Potrdi geslo"
                id="password"
                type="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary">
              Pošlji &nbsp;
              <v-icon>mdi-send</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    formData: {
      username: null,
      email: null,
      password: null
    }
  }),
  methods: {
    signup() {
      this.$store.dispatch("signup", this.formData);
    }
  }
};
</script>

<style scoped></style>
