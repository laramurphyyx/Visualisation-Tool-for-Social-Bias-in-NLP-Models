import { initializeApp } from 'firebase/app';
import "firebase/firestore";
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyDXSxlAhg0RvOX-EMSR7YD_Rip_FuKGxHI",
  authDomain: "ca4021-33e09.firebaseapp.com",
  projectId: "ca4021-33e09",
  storageBucket: "ca4021-33e09.appspot.com",
  messagingSenderId: "284061839526",
  appId: "1:284061839526:web:5e86197376908ab9774467"
};

const app = initializeApp(firebaseConfig);

const db = getFirestore(app);

export default db;