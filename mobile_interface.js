import React, { useState } from 'react';

const MobileInterface = () => {
    const [userInput, setUserInput] = useState('');
    const [assistantResponse, setAssistantResponse] = useState('');

    const handleUserInput = async (input) => {
        setUserInput(input);

        const response = await fetch('/process_user_input', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: input }),
        });

        const responseData = await response.json();
        setAssistantResponse(responseData.response);
    };

    return (
        <div>
            <input
                type="text"
                value={userInput}
                onChange={(e) => handleUserInput(e.target.value)}
            />
            <div>
                <strong>Assistant Response:</strong> {assistantResponse}
            </div>
        </div>
    );
};

export default MobileInterface;
