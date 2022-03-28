import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.7/firebase-app.js";
import { getFirestore, addDoc, collection, getDocs, query, where, updateDoc} 
from "https://www.gstatic.com/firebasejs/9.6.7/firebase-firestore.js";

// admin@test.com + password123

const firebaseConfig = {
    apiKey: "AIzaSyAbmjyY5Oolx-MQzJJBqLtzUu6Q5ObHCt8",
    authDomain: "scentproductionsllc.firebaseapp.com",
    projectId: "scentproductionsllc",
    storageBucket: "scentproductionsllc.appspot.com",
    messagingSenderId: "563963156196",
    appId: "1:563963156196:web:715df1c22e35b0817ebef1",
    measurementId: "G-Y197YY3QN5"
    };

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

document.addEventListener('submit', function login(e) {
    e.preventDefault();
    var userEmail = document.getElementById("email").value;
    var userPass = document.getElementById("password").value;


    signInWithEmailAndPassword(auth, userEmail, userPass)
    .then((userCredential) => {
    // Signed in
        const user = userCredential.user;
        window.location.replace("testSucc.html");
    // ...
    })
    .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
    });

});