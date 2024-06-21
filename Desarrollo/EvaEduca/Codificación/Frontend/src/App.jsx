import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import F12Main from "./pages/F12Main";

import DbAlumno from "./pages/DbAlumno/DbAlumno";
import DbPrpofesor from "./pages/DBProfesor/DbPrpofesor";
import DbSuperAdministrador from "./pages/DbSuperAdministrador/DbSuperAdministrador";
import DbSuperAdministrador1 from "./pages/DbSuperAdministrador1/DbSuperAdministrador1";
import InicioEe from "./pages/Inicio/InicioEe";
import Login from "./pages/Login/Login";
import Registrarse from "./pages/Registrarse/Registrarse";
import RegistroAlumno from "./pages/RegistroAlumno/RegistroAlumno";
import RegistroAlumnoIi from "./pages/RegistroAlumno1/RegistroAlumnoIi";
import RegistroProfesor from "./pages/RegistroProfesor/RegistroProfesor";
import RegistroProfesorIi from "./pages/RegistroProfesor1/RegistroProfesorIi";

const router = createBrowserRouter([
  { path: "/", element: <F12Main /> },
  { path: "/DbAlumno", element: <DbAlumno /> },
  { path: "/DbPrpofesor", element: <DbPrpofesor /> },
  { path: "/DbSuperAdministrador", element: <DbSuperAdministrador /> },
  { path: "/DbSuperAdministrador1", element: <DbSuperAdministrador1 /> },
  { path: "/InicioEe", element: <InicioEe /> },
  { path: "/Login", element: <Login /> },
  { path: "/Registrarse", element: <Registrarse /> },
  { path: "/RegistroAlumno", element: <RegistroAlumno /> },
  { path: "/RegistroAlumnoIi", element: <RegistroAlumnoIi /> },
  { path: "/RegistroProfesor", element: <RegistroProfesor /> },
  { path: "/RegistroProfesorIi", element: <RegistroProfesorIi /> },
]);

export default function App() {
  return <RouterProvider router={router} />;
}
