/** 
 * A component to select icons, but it's very gross and didn't work...
 */

import { IconDefinition } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCat, faDog, faFish, faFrog, faHorse, faArrowRight, faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import Slider, { Settings } from 'react-slick';
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
import styled from 'styled-components';

const SliderWrapper = styled.div`
  width: 100px;
  height: 100px;
`;

const IconWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;

const Arrow = styled.div`
  color: #000;
  cursor: pointer;
`;

interface ArrowProps {
  onClick: () => void;
}

interface IconCarouselProps {
  onIconChange: (icon: IconDefinition) => void;
}

const IconCarousel: React.FC<IconCarouselProps> = ({ onIconChange }) => {
  const icons: IconDefinition[] = [faCat, faDog, faFish, faFrog, faHorse];

  const SliderWrapper = styled.div`
  width: 100px;
  height: 100px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const Arrow = styled.div`
  color: #000;
  cursor: pointer;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
`;

const NextArrow: React.FC<ArrowProps> = (props) => (
  <Arrow {...props} style={{ right: 0 }}>
    <FontAwesomeIcon icon={faArrowRight} />
  </Arrow>
);

const PrevArrow: React.FC<ArrowProps> = (props) => (
  <Arrow {...props} style={{ left: 0 }}>
    <FontAwesomeIcon icon={faArrowLeft} />
  </Arrow>
);
  
  const settings: Settings = {
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    // nextArrow: <NextArrow />,
    // prevArrow: <PrevArrow />,
    afterChange: (current) => onIconChange(icons[current])
  };

  return (
    <SliderWrapper>
      <Slider {...settings}>
        {icons.map((iconOption, index) => (
          <IconWrapper key={index}>
            <FontAwesomeIcon icon={iconOption} size="1x" />
          </IconWrapper>
        ))}
      </Slider>
    </SliderWrapper>
  );
}

export default IconCarousel;