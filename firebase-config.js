// firebase-config.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, signOut, onAuthStateChanged, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore, doc, setDoc, getDoc, onSnapshot, collection, addDoc, query, orderBy, limit, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyA9eTc8d-AzQMtgLYqZ8DAzYgFnTI4YgNo",
  authDomain: "pushti-study-hub-c5961.firebaseapp.com",
  projectId: "pushti-study-hub-c5961",
  storageBucket: "pushti-study-hub-c5961.firebasestorage.app",
  messagingSenderId: "385702072981",
  appId: "1:385702072981:web:c0a4c656642f50a674019c",
  measurementId: "G-T1WE5CGRRL"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, db, signInWithEmailAndPassword, signOut, onAuthStateChanged, createUserWithEmailAndPassword, doc, setDoc, getDoc, onSnapshot, collection, addDoc, query, orderBy, limit, serverTimestamp };
