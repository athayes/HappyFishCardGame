// IconSelector.tsx
import React, { useState } from 'react';
import { IconDefinition } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCat, faDog, faFish, faFrog, faHorse, faKiwiBird } from '@fortawesome/free-solid-svg-icons';

interface IconOption {
  value: string;
  icon: IconDefinition;
}

interface IconSelectorProps {
  onIconChange: (icon: IconDefinition) => void;
}

const IconSelector: React.FC<IconSelectorProps> = ({ onIconChange }) => {
  const [selectedIcon, setSelectedIcon] = useState<IconDefinition>(faCat);
  const [selectedValue, setSelectedValue] = useState<string>('cat');

  const iconOptions: IconOption[] = [
    { value: 'cat', icon: faCat },
    { value: 'dog', icon: faDog },
    { value: 'fish', icon: faFish },
    { value: 'frog', icon: faFrog },
    { value: 'horse', icon: faHorse },
    { value: 'kiwi bird', icon: faKiwiBird }
  ];

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedOption = iconOptions.find(option => option.value === event.target.value);
    if (selectedOption) {
      setSelectedIcon(selectedOption.icon);
      setSelectedValue(selectedOption.value);
      onIconChange(selectedOption.icon);
    }
  };

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
      <select onChange={handleChange} value={selectedValue}>
        {iconOptions.map(option => (
          <option key={option.value} value={option.value}>
            {option.value}
          </option>
        ))}
      </select>
      <FontAwesomeIcon icon={selectedIcon} size="2x" />
    </div>
  );
};

export default IconSelector;