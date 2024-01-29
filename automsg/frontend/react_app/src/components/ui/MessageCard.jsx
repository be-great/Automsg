import Card from 'react-bootstrap/Card';
import { BsThreeDotsVertical } from "react-icons/bs";
import { CgProfile } from "react-icons/cg";
import { FaWhatsapp } from "react-icons/fa";

const MessageCard = () => {
  return <div>
    <Card>
      <Card.Body className='bg-secondary'>
        <div className='d-flex flex-column'>
            <div className='d-flex justify-content-between'>
                <h3 className='text-primary'>Today (09:30 AM)</h3>
                <BsThreeDotsVertical className='text-primary fs-3'/>
            </div>
            <div className='d-flex'>
                <div>
                    <button type="button" className="btn btn-secondary position-relative border border-danger">
                    <CgProfile className=' bg-secondary fs-1 border border-danger'/>
                        <span className="position-absolute top-100 start-0  translate-middle badge rounded-pill bg-success border border-danger"><FaWhatsapp /> <span className="visually-hidden">unread messages</span></span>
                    </button>
                </div>
                <p className='pt-2'>Have you got any plans for today? Have a nice day</p>
            </div>

        </div>
      </Card.Body>
    </Card>
  </div>;
};

export default MessageCard;
