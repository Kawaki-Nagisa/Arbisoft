import { Stack } from "@mui/material"
import { categories } from "../utils/constants"

const SideBar = ({selectedCategory, setSelectedCategory}) => (
    <Stack direction="row" 
    sx={{ overflowY: 'auto', height: { sx: 'auto', md: '95%' }, flexDirection: {md: 'column'} }}
    >

    {categories.map((category) => (
    <button  className="category-btn" 
    onClick={()=>setSelectedCategory(category.name)}
    style={{ ":hover" : {bgcolor: "gray",  color: "white"},  background: category.name === selectedCategory && 'gray', color: 'white' }}
    key={category.name}>
        <span style={{ marginRight: '15px'}}>{category.icon}</span>
        <span >{category.name}</span>
    </button>))}

    </Stack>
)

export default SideBar