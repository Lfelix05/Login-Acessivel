// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBs1O9F7FH6Z_-txsPEpRHmOYwvvrtvxaA",
  authDomain: "easyway-24904.firebaseapp.com",
  projectId: "easyway-24904",
  storageBucket: "easyway-24904.appspot.com",
  messagingSenderId: "865515602045",
  appId: "1:865515602045:web:8f92179088be41bea0f114",
  measurementId: "G-RDMW5BH4WJ"
};


// Inicializa o Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();

// Função para registrar um novo usuário
function registerUser(name, email, password, accessibility, favorites) {
  return auth.createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      return db.collection("users").doc(userCredential.user.uid).set({
        name: name,
        email: email,
        accessibility: accessibility,
        favorites: favorites
      });
    });
}

window.registerUser = registerUser;