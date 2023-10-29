import React, { useState } from 'react';


const SearchBar = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (e) => {
    e.preventDefault();
    onSearch(searchTerm);
  };

  return (
    <div className="flex items-center justify-center py-10 h-fit bg-gray-200">
      <form className="flex items-center">
        <input
          type="text"
          className="bg-transparent border-b-2 border-gray-500 focus:outline-none focus:border-gray-800 text-gray-800 px-4 py-2 rounded-l-lg"
          placeholder="Enter state name"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button
          className="bg-transparent text-gray-500 px-4 py-2 rounded-r-lg hover:text-amber-800"
          onClick={handleSearch}
        >
          Search
        </button>
      </form>
    </div>
  );
};

export default SearchBar;
