# Simple fix script - remove problematic emoji section and replace with clean code
import re

# Read the file
with open('src/app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the problematic section (lines 985-1014)
# Replace the complex emoji HTML section with simple streamlit components

old_pattern = r'''        
        st\.markdown\("### 👥 Project Team"\)
        
       st\.markdown\(""".*?"""(?:, unsafe_allow_html=True)?\)'''

new_code = '''        
        st.markdown("### 👥 Project Team")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("**Team Leader**\\nRanjeet Kumar\\n*Full Stack Development, ML Engineering*")
        with col2:
            st.info("**Team Member**\\nMadhuri Challagundla\\n*Data Analysis, UI/UX Design*")
        
        st.info("**University:** IIT Roorkee | **Project:** AI for Rural Innovation & Sustainable Systems | **Year:** 2026")'''

# Use simple string replacement for the known problematic section
# Find the start of the team section
team_start = content.find('st.markdown("### 👥 Project Team")')
if team_start > 0:
    # Find the end (next st.markdown after that)
    search_from = team_start + 100
    next_markdown = content.find('st.markdown("""', search_from)
    if next_markdown > 0:
        # Find the end of this markdown block
        end_of_block = content.find('""", unsafe_allow_html=True)', search_from)
        if end_of_block > 0:
            end_of_block += len('""", unsafe_allow_html=True)')
            # Replace this entire section
            content = content[:team_start] + new_code + content[end_of_block:]
            
            # Write back
            with open('src /app.py', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Fixed successfully!")
        else:
            print("Could not find end of markdown block")
    else:
        print(f"Could not find next markdown. Next char: {content[search_from:search_from+50]}")
else:
    print("Could not find team section")
