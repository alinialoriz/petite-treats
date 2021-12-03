
// Set Error Message
function setError(input, errormsg) {
	const formGroup = input.parentElement;
	const inputAlert = formGroup.querySelector(".input-alert");
	formGroup.className = "form-group error";
	inputAlert.innerText = errormsg;
}

// Set Success Message
function setSuccess(input) {
	const formGroup = input.parentElement;
	formGroup.className = "form-group success";
}

// Check Valid Email
function validEmail(email) {
	const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(String(email).toLowerCase());
}

// Form Validation Check for Newsletter Form
function validateNeswletterForm(form) {
	if (form.name.value.trim() === "") {
		setError(form.name, "Name cannot be blank");
		return false;
	} else {
		setSuccess(form.name);
	}

	if (form.email.value.trim() === "") {
		setError(form.email, "Email cannot be blank");
		return false;
	} else if (!validEmail(form.email.value.trim())) {
		setError(form.email, "Email is not valid");
		return false;
	} else {
		setSuccess(form.email);
	}
	
	
    if(!form.agree.checked)
    {
        setError(form.agree,"Can't proceed as you didn't agree to the terms!")
        return false;
    }
    else {
        setSuccess(form.agree)
    }
    
    
	return true;
}

// Form Validation Check for Contact Form
function validateContactForm(form) {
	if (form.name.value.trim() === "") {
		setError(form.name, "Name cannot be blank");
		return false;
	} else {
		setSuccess(form.name);
	}

	if (form.email.value.trim() === "") {
		setError(form.email, "Email cannot be blank");
		return false;
	} else if (!validEmail(form.email.value.trim())) {
		setError(form.email, "Email is not valid");
		return false;
	} else {
		setSuccess(form.email);
	}
	
    if (form.message.value.trim() === "") {
		setError(form.message, "Message cannot be blank");
		return false;
	} else {
		setSuccess(form.message);
	}
    
	return true;
}

// Form Validation Check for Order Form
function validateOrderForm(form) {
	if (form.name.value.trim() === "") {
		setError(form.name, "Name cannot be blank");
		return false;
	} else {
		setSuccess(form.name);
	}

	if (form.email.value.trim() === "") {
		setError(form.email, "Email cannot be blank");
		return false;
	} else if (!validEmail(form.email.value.trim())) {
		setError(form.email, "Email is not valid");
		return false;
	} else {
		setSuccess(form.email);
	}
	
    if(!form.pickup.checked)
    {
        setError(form.pickup,"We only accept in-store pick up for all orders. Check this option to proceed.")
        return false;
    }
    else {
        setSuccess(form.pickup)
    }
    
	return true;
}
