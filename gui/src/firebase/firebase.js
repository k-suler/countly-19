// This import loads the firebase namespace.
import firebase from 'firebase/app';

// These imports load individual services into the firebase namespace.
import 'firebase/auth';
import 'firebase/database';
import 'firebase/firestore';
import 'firebase/storage';
import 'firebase/analytics'



// firebase init - add your own config here
const firebaseConfig = {
    apiKey: "AIzaSyD3Q1oHXOFNtRB7vxu63rtQk8aI18oUSg4",
    authDomain: "countly-19.firebaseapp.com",
    databaseURL: "https://countly-19-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "countly-19",
    storageBucket: "countly-19.appspot.com",
    messagingSenderId: "809868506187",
    appId: "1:809868506187:web:4f987deadd25749dab49ce",
    measurementId: "G-DMS9174PCJ"
};
firebase.initializeApp(firebaseConfig)

// export default firebase.database();
// utils
const db = firebase.firestore()
const database = firebase.database();
const auth = firebase.auth()

// collection references
const storesCollection = db.collection('stores')
// const postsCollection = db.collection('posts')
// const commentsCollection = db.collection('comments')
// const likesCollection = db.collection('likes')

// export utils/refs
export {
    db,
    auth,
    database,
    storesCollection
    // usersCollection,
    // postsCollection,
    // commentsCollection,
    // likesCollection
}
