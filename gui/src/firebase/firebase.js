// This import loads the firebase namespace.
import firebase from 'firebase/app';

// These imports load individual services into the firebase namespace.
import 'firebase/auth';
import 'firebase/database';
import 'firebase/firestore';
import 'firebase/storage';
import 'firebase/analytics'



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
