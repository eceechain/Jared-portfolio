import React from 'react';
import { NavLink } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <NavLink to="/" end>
        Home
      </NavLink>
      <NavLink to="/about">
        About
      </NavLink>
      <NavLink to="/blogs">
        Blogs
      </NavLink>
      <NavLink to="/contacts">
        Contacts
      </NavLink>
      <NavLink to="/projects">
        Projects
      </NavLink>
      <NavLink to="/skills">
        Skills
      </NavLink>
      
    </nav>
  );
}

export default Navbar;
