import {useRef, useEffect} from 'react';

const App = () => {
    const ref = useRef(null);
  
    useEffect(() => {
      const handleClick = event => {
        console.log('Button clicked');
      };
  
      const element = ref.current;
  
      element.addEventListener('click', handleClick);
  
      return () => {
        element.removeEventListener('click', handleClick);
      };
    }, []);
  
    return (
      <div>
        <button ref={ref}>Click</button>
      </div>
    );
  };
  
  export default App;
  