import React from 'react'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Home";
import About from "./About";
import Blogs from './Blogs';
import Contacts from './Contacts';
import Projects from './Projects';
import Skills from './Skills';
import Navbar from './Navbar';


function Dashboard() {
  return (
    <Router>
    {/* Navbar should be inside the Router so it can use the Link component */}
    <Navbar />

    {/* Define the routes for different components */}
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/blogs" element={<Blogs />} />
      <Route path="/contacts" element={<Contacts />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/projects" element={<Projects />} />
      <Route path="/skills" element={<Skills />} />
    </Routes>
  </Router>
  )
}

export default Dashboard
