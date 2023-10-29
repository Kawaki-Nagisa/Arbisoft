import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {Box} from '@mui/material'

import { Navbar, Feed, SearchFeed } from './componnets'

const App = () => (
    <BrowserRouter>
        <Box sx={{ backgroundColor: "#121415"}}>
            <Navbar />
            <Routes>
                <Route path="/" exact element={<Feed />} />
                <Route path="/search/:searchTerm" element={<SearchFeed />} />
            </Routes>
        </Box>
    </BrowserRouter>
)

export default App