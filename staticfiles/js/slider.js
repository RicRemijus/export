document.addEventListener('DOMContentLoaded', function(){
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const carouselInner = document.querySelector('.carousel-inner');
    const carouselItems = document.querySelectorAll('.carousel-item');
    const indicators = document.querySelectorAll('.indicator');

    let currentIndex = 0;
    let totalItems = carouselItems.length;
    let autoSlideInterval;

    //update the carousel position and active indicator
    function updateCarousel (){
        //Move carousel item bys by changing the transform
        const offset = -currentIndex * 100; //move by 100% width of the item
        carouselInner.style.transform =`translateX(${offset}%)`;

        //update the indicator's background color to show active
        indicators.forEach((indicator, index) =>{
            if(index === currentIndex){
                indicator.classList.add('bg-green-500');
                indicator.classList.remove('bg-gray-50');
            }else{
                indicator.classList.remove('bg-green-500');
                indicator.classList.add('bg-gray-50');
            }
        });
    }
    //show prevoius image
    prevBtn.addEventListener('click', function(){
        currentIndex = (currentIndex ===  0) ? totalItems - 1 : currentIndex - 1;
        updateCarousel();
    });
    //show next iamge
    nextBtn.addEventListener('click', function(){
        currentIndex = (currentIndex === totalItems - 1) ? 0 : currentIndex + 1;
        updateCarousel();
    });
    //Automatically cycle through images
    function startAutoSlide(){
        autoSlideInterval = setInterval(function (){
            currentIndex = (currentIndex === totalItems - 1) ? 0 : currentIndex + 1;
            updateCarousel();
        }, 3000);//change image every 3 seconds
    }
    //Stop autoslide when mouse over carousel
    // document.querySelector('.carousel-container').addEventListener('mouseenter',function(){
    //     clearInterval(autoSlideInterval);
    // })
    // //Resume autoslide when mouse leave carousel
    // document.querySelector('.carousel-container').addEventListener('mouseleave',function(){
    //     startAutoSlide();
    // })
    //start the carousel autoslide on page load
    startAutoSlide();
    //initialize carousel
    updateCarousel();
    //update carousel when an indicator is clicked
    indicators.forEach((indicator) =>{
        indicator.addEventListener('click', function(){
            currentIndex = parseInt(indicator.getAttribute('data-index'));
            updateCarousel();
        });
    });
});